from abc import ABC
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD, CONF_SCAN_INTERVAL
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from httpx import ConnectError
from .api_client.client import AuthenticatedClient
from .api_client.api.authentication import (
    api_v2_auth_token_create,
)
from .api_client.api.plant import api_v2_plant_list, api_v2_plant_retrieve
from .const import DEFAULT_SCAN_INTERVAL, VISION_BASE_URL
from datetime import timedelta
import logging


_LOGGER = logging.getLogger(__name__)


class VisionPlantCoordinator(DataUpdateCoordinator):
    def __init__(
        self,
        hass: HomeAssistant,
        client: AuthenticatedClient,
        uuid: str,
        name: str,
        scan_interval: int,
        has_energymeter: bool,
        has_production: bool,
    ) -> None:
        self.client = None
        self.hass = hass
        self.client = client
        self.uuid = uuid
        self.capabilities = {"has_energymeter": False, "has_production": False}
        self.current_values = None
        self.scan_interval = scan_interval
        self.has_energymeter = has_energymeter
        self.has_production = has_production
        super().__init__(
            hass,
            _LOGGER,
            name=f"GEF Vision {self.uuid}",
            update_interval=timedelta(seconds=self.scan_interval),
        )

    async def _async_update_data(self):
        try:
            data = await api_v2_plant_retrieve.asyncio_detailed(
                client=self.client, uuid=self.uuid
            )
            if data.status_code == 200:
                self.current_values = data.parsed
            else:
                _LOGGER.error(f"Failed to fetch data: {data}")
                self.current_values = None
        except Exception as err:
            _LOGGER.exception(f"Update failed for plant {self.uuid}")
            self.current_values = None
            raise UpdateFailed(err)
