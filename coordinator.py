import logging
from datetime import timedelta
from typing import List
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from httpx import ConnectError, ConnectTimeout
from .api_client.api.authentication import (
    api_v2_auth_token_create,
)
from .api_client.client import Client, AuthenticatedClient
from .api_client.models import (
    AuthToken,
    OverrideControl,
    Energymeter,
    Inverter,
    Control,
    Sensor,
    Production,
    Consumption,
)
from .api_client.api.control import (
    api_v2_plant_device_control_list,
    api_v2_plant_device_control_off_create,
    api_v2_plant_device_control_on_create,
)
from .api_client.api.sensor import api_v2_plant_device_sensor_list
from .api_client.api.production import (
    api_v2_plant_device_inverter_list,
    api_v2_plant_production_retrieve,
)
from .api_client.api.consumption import (
    api_v2_plant_consumption_retrieve,
    api_v2_plant_device_energymeter_list,
)
from .const import VISION_BASE_URL, ERROR_SCAN_INTERVAL


_LOGGER = logging.getLogger(__name__)


class VisionUpdateCoordinator(DataUpdateCoordinator):
    def __init__(
        self,
        hass: HomeAssistant,
        client: AuthenticatedClient,
        uuid: str,
        name: str,
        scan_interval: int,
        energymeters: List[Energymeter],
        inverters: List[Inverter],
        controls: List[Control],
        sensors: List[Sensor],
        production: Production,
        consumption: Consumption,
    ) -> None:
        self.fail_cnt: int = 0
        self.current_interval: int = scan_interval
        self.scan_interval: int = scan_interval
        self.client: AuthenticatedClient = client
        self.uuid: str = uuid
        self.energymeters = energymeters
        self.inverters = inverters
        self.controls = controls
        self.sensors = sensors
        self.production = production
        self.consumption = consumption
        self.has_energymeters = True if self.energymeters else False
        self.has_sensors = True if self.sensors else False
        self.has_production = True if self.inverters else False
        self.has_controls = True if self.controls else False
        self.has_sensors = True if self.sensors else False

        super().__init__(
            hass=hass,
            logger=_LOGGER,
            name=name,
            update_interval=timedelta(seconds=scan_interval),
        )

    @property
    def grid_interface(self):
        for meter in self.energymeters:
            if meter.meter_type == 0:
                return meter
        return None

    def get_control(self, control_id: int):
        for control in self.controls:
            if control.id == control_id:
                return control.to_dict()
        raise ValueError("Unknown control ID")

    def get_energymeter_values(self, meter_id: int):
        if meter_id == "total-consumption":
            return self.consumption.to_dict()
        elif meter_id == "grid-interface":
            return self.grid_interface.to_dict()
        for meter in self.energymeters:
            if meter.id == meter_id:
                return meter.to_dict()
        raise ValueError("Unkown meter ID")

    def get_inverter_values(self, inverter_id: int | str):
        if inverter_id == "total-production":
            return self.get_total_production()
        for inverter in self.inverters:
            if inverter.id == inverter_id:
                return inverter.to_dict()
        raise ValueError("Unknown inverter ID:", inverter_id)

    def get_total_production(self):
        return self.production.primary.to_dict() if self.production else {}

    def get_sensor_values(self, sensor_id: int):
        for sensor in self.sensors:
            if sensor.id == sensor_id:
                return sensor.to_dict()
        raise ValueError("Unknown sensor ID:", sensor_id)

    async def _async_update_data(self):
        if self.has_production:
            self.inverters = await self.fetch_endpoint(
                endpoint=api_v2_plant_device_inverter_list,
                plant_uuid=self.uuid,
                client=self.client,
            )
            # In case of multiple inverters, fetch total production
            if len(self.inverters) > 1:
                self.production = await self.fetch_endpoint(
                    endpoint=api_v2_plant_production_retrieve,
                    uuid=self.uuid,
                    client=self.client,
                )
        if self.has_energymeters:
            self.energymeters = await self.fetch_endpoint(
                endpoint=api_v2_plant_device_energymeter_list,
                plant_uuid=self.uuid,
                client=self.client,
            )

        if self.grid_interface:
            self.consumption = await self.fetch_endpoint(
                endpoint=api_v2_plant_consumption_retrieve,
                uuid=self.uuid,
                client=self.client,
            )

        if self.has_controls:
            self.controls = await self.fetch_endpoint(
                endpoint=api_v2_plant_device_control_list,
                plant_uuid=self.uuid,
                client=self.client,
            )

        if self.has_sensors:
            self.sensors = await self.fetch_endpoint(
                endpoint=api_v2_plant_device_sensor_list,
                plant_uuid=self.uuid,
                client=self.client,
            )

    async def fetch_endpoint(self, endpoint, **kwargs):
        try:
            response = await endpoint.asyncio_detailed(**kwargs)
            if response.status_code == 200:
                if self.current_interval == ERROR_SCAN_INTERVAL:
                    self.current_interval = self.scan_interval
                    self.update_interval = timedelta(seconds=self.scan_interval)
                self.fail_cnt = 0
                return response.parsed
            elif response.status_code == 403:
                raise ConfigEntryAuthFailed(
                    f"Authentication failed for plant {self.uuid}"
                )
            else:
                raise UpdateFailed(f"Unexpected return code {response.status_code}")
        except (ConnectError, ConnectTimeout) as exc:
            self.fail_cnt += 1
            if self.fail_cnt > 3:
                self.current_interval = ERROR_SCAN_INTERVAL
                self.update_interval = timedelta(seconds=ERROR_SCAN_INTERVAL)
                raise UpdateFailed(
                    f"Failed to update data for plant {self.uuid}"
                ) from exc

    @classmethod
    async def authenticate_user(cls, username: str, password: str):
        auth = AuthToken(
            username=username,
            password=password,
            token="",
        )
        client = Client(VISION_BASE_URL)
        token = await api_v2_auth_token_create.asyncio_detailed(
            client=client, json_body=auth
        )
        if token.status_code != 200:
            return False
        return AuthenticatedClient(
            base_url=VISION_BASE_URL, token=token.parsed.token, prefix="Token"
        )

    async def set_control_state(self, control_id: int, state: bool):
        if state:
            await api_v2_plant_device_control_on_create.asyncio(
                plant_uuid=self.uuid,
                id=control_id,
                client=self.client,
                json_body=OverrideControl(),
            )
        else:
            await api_v2_plant_device_control_off_create.asyncio(
                plant_uuid=self.uuid,
                id=control_id,
                client=self.client,
                json_body=OverrideControl(),
            )
