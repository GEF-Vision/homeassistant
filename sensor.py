import logging
import operator
from functools import reduce
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import (
    GRID_INTERFACE_ENTITY_DESCRIPTIONS,
    CONSUMPTION_ENTITY_DESCRIPTIONS,
    PRODUCTION_ENTITY_DESCRIPTIONS,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)


class VisionAPISensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, description):
        super().__init__(coordinator)
        key = description.key.replace("-", "_")
        self.entity_description = description
        self._attr_name = f"{coordinator.name} {description.name}"
        self._attr_unique_id = f"{coordinator.unique_id}_{key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.unique_id)},
            manufacturer="GreenEnergy Finland Oy",
            name=coordinator.name,
        )

    @property
    def native_value(self):
        return reduce(
            operator.getitem,
            self.entity_description.json_path.split("-"),
            self.coordinator.values.get(self.entity_description.json_key, {}),
        )


async def async_setup_entry(hass, entry, async_add_entities) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]
    if coordinator.capabilities["has_energymeter"]:
        async_add_entities(
            VisionAPISensor(coordinator, description)
            for description in GRID_INTERFACE_ENTITY_DESCRIPTIONS
        )
        async_add_entities(
            VisionAPISensor(coordinator, description)
            for description in CONSUMPTION_ENTITY_DESCRIPTIONS
        )
    if coordinator.capabilities["has_production"]:
        async_add_entities(
            VisionAPISensor(coordinator, description)
            for description in PRODUCTION_ENTITY_DESCRIPTIONS
        )
