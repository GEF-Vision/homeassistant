"""The GEF Vision integration."""
from __future__ import annotations
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    Platform,
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_SCAN_INTERVAL,
)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from httpx import ConnectError
from .const import DOMAIN, VISION_BASE_URL
from .coordinator import VisionPlantCoordinator
from .api_client.models import Plant, AuthToken
from .api_client.client import Client, AuthenticatedClient
from .api_client.api.plant import api_v2_plant_list
from .api_client.api.authentication import api_v2_auth_token_create
import logging
from typing import List


PLATFORMS: list[Platform] = [Platform.SENSOR]

_LOGGER = logging.getLogger(__name__)


class GEFVision:
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry):
        self.plant_coordinators: List[VisionPlantCoordinator] = []
        self.config = entry
        self.hass = hass
        self.client = None

    async def initialize(self):
        try:
            self.client = await VisionPlantCoordinator.authenticate_user(
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
        # Fetch plant list
        try:
            data = await api_v2_plant_list.asyncio(client=self.client)
            if not data or not data.results:
                _LOGGER.error("User has no plants!")
            # Create coordinators
            for plant in data.results:
                has_production = True if getattr(plant, "production") else False
                has_energymeter = True if getattr(plant, "consumption") else False
                coordinator = VisionPlantCoordinator(
                    hass=self.hass,
                    client=self.client,
                    uuid=plant.uuid,
                    name=f"{DOMAIN}_plants_{plant.uuid}",
                    scan_interval=self.config.data[CONF_SCAN_INTERVAL],
                    has_energymeter=has_energymeter,
                    has_production=has_production,
                )
                await coordinator.async_config_entry_first_refresh()
                self.plant_coordinators.append(coordinator)
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
