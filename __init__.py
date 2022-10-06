"""The GEF Vision integration."""
from __future__ import annotations
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    Platform,
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_SCAN_INTERVAL,
    CONF_UNIQUE_ID,
)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from httpx import ConnectError
from .const import (
    DOMAIN,
    VISION_BASE_URL,
    VISION_DEVICE_TYPE_INVERTER,
    VISION_DEVICE_TYPE_ENERGYMETER,
    VISION_DEVICE_TYPE_SENSOR,
    VISION_DEVICE_TYPE_CONTROL,
    VISION_METER_TYPE_GRID_INTERFACE,
    VISION_METER_TYPE_CONSUMPTION,
)
from .coordinator import VisionUpdateCoordinator
from .api_client.models import (
    Plant,
    AuthToken,
    Control,
    Inverter,
    Energymeter,
    Sensor,
    Device,
)
from .api_client.client import Client, AuthenticatedClient
from .api_client.api.device import api_v2_plant_device_list
from .api_client.api.plant import api_v2_plant_retrieve
from .api_client.api.grid_interface import api_v2_plant_grid_interface_retrieve
from .api_client.api.consumption import (
    api_v2_plant_device_energymeter_list,
    api_v2_plant_consumption_retrieve,
)
from .api_client.api.production import (
    api_v2_plant_device_inverter_list,
    api_v2_plant_production_retrieve,
)
from .api_client.api.sensor import api_v2_plant_device_sensor_list
from .api_client.api.control import api_v2_plant_device_control_list
import logging
from typing import List
from asyncio import Lock


PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.SWITCH]

_LOGGER = logging.getLogger(__name__)


class GEFVision:
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry):
        self.coordinator: VisionUpdateCoordinator | None = None
        self.inverters: List[Inverter] = []
        self.energymeters: List[Energymeter] = []
        self.sensors: List[Sensor] = []
        self.controls: List[Control] = []
        self.config: ConfigEntry = entry
        self.hass: HomeAssistant = hass
        self.client_mutex: Lock = Lock()
        self.client: AuthenticatedClient = None

    async def initialize(self):
        try:
            self.client = await VisionUpdateCoordinator.authenticate_user(
                self.config.data[CONF_USERNAME], self.config.data[CONF_PASSWORD]
            )
            if not self.client:
                raise ConfigEntryAuthFailed(
                    f"Invalid Vision credentials for {self.config.data[CONF_USERNAME]}"
                )
        except ConnectError as err:
            raise ConfigEntryNotReady(
                f"Connection failed with Vision - cannot authenticate: {self.config.data[CONF_USERNAME]}"
            ) from err
        try:
            # Fetch plant info
            plant = await api_v2_plant_retrieve.asyncio(
                client=self.client, uuid=self.config.data[CONF_UNIQUE_ID]
            )
            # Fetch energymeters
            meters = await api_v2_plant_device_energymeter_list.asyncio(
                client=self.client, plant_uuid=self.config.data[CONF_UNIQUE_ID]
            )
            inverters = await api_v2_plant_device_inverter_list.asyncio(
                client=self.client, plant_uuid=self.config.data[CONF_UNIQUE_ID]
            )
            controls = await api_v2_plant_device_control_list.asyncio(
                client=self.client, plant_uuid=self.config.data[CONF_UNIQUE_ID]
            )
            sensors = await api_v2_plant_device_sensor_list.asyncio(
                client=self.client, plant_uuid=self.config.data[CONF_UNIQUE_ID]
            )
            production = await api_v2_plant_production_retrieve.asyncio(
                client=self.client, uuid=self.config.data[CONF_UNIQUE_ID]
            )
            consumption = await api_v2_plant_consumption_retrieve.asyncio(
                client=self.client, uuid=self.config.data[CONF_UNIQUE_ID]
            )
            self.coordinator = VisionUpdateCoordinator(
                self.hass,
                self.client,
                self.config.data[CONF_UNIQUE_ID],
                f"{DOMAIN}-plant-{self.config.data[CONF_UNIQUE_ID]}",
                self.config.data[CONF_SCAN_INTERVAL],
                meters,
                inverters,
                controls,
                sensors,
                production,
                consumption,
            )

        except ConnectError as err:
            raise ConfigEntryNotReady(
                f"Connection failed to {VISION_BASE_URL}"
            ) from err


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up GEF Vision from a config entry."""
    client = GEFVision(hass, entry)
    await client.initialize()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = client
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    err = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return err
