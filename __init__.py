"""The GEF Vision integration."""
from __future__ import annotations
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from .client import VisionClient
from .const import DOMAIN, HAS_ENERGYMETER, HAS_INVERTER, CLIENT, POLL_INTERVAL
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.SENSOR]

_LOGGER = logging.getLogger(__name__)


class GEFVisionCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.hass = hass
        self.config = entry
        self.client = VisionClient(
            entry.data["username"], entry.data["password"], entry.data["plant_uuid"]
        )
        self.unique_id = entry.entry_id
        self.capabilities = {"has_energymeter": False, "has_production": False}
        self.values = {}
        interval = entry.data.get("poll_interval_s", POLL_INTERVAL)
        _LOGGER.info("Using poll interval of %u seconds", interval)
        super().__init__(
            hass, _LOGGER, name="GEFVision", update_interval=timedelta(seconds=interval)
        )

    async def initialize(self) -> None:
        await self.client.authenticate()
        self.capabilities = await self.client.get_capabilities(
            self.config.data["plant_uuid"]
        )
        print(self.capabilities)

    async def _async_update_data(self):
        try:
            data = await self.client.fetch_plant(self.config.data["plant_uuid"])
            self.values = data
        except Exception as err:
            raise UpdateFailed(err)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up GEF Vision from a config entry."""
    client = GEFVisionCoordinator(hass, entry)
    await client.initialize()
    await client.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = client
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    err = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    return err
