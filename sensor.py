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
    def __init__(self, coordinator, description, plant_uuid):
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_name = f"{description.name}"
        self._attr_unique_id = f"{plant_uuid}-{description.key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.uuid)},
            manufacturer="GreenEnergy Finland Oy",
            name=coordinator.name,
        )

    @property
    def native_value(self):
        data = self.coordinator.current_values
        if not data:
            return None
        try:
            data = data.to_dict().get(self.entity_description.json_key)
            if not data:
                _LOGGER.warning("No data")
            path = self.entity_description.json_path.split("-")
            value = reduce(
                operator.getitem,
                path,
                data,
            )
            if value is None:
                _LOGGER.warning(
                    f"Could not find value for {self.entity_description.json_key}/{path}"
                )
            return value
        except Exception as e:
            _LOGGER.exception(e)
            return None


async def async_setup_entry(hass, entry, async_add_entities) -> None:
    base = hass.data[DOMAIN][entry.entry_id]
    entities = []
    for coordinator in base.plant_coordinators:
        uuid = coordinator.uuid
        if coordinator.has_energymeter:
            for description in GRID_INTERFACE_ENTITY_DESCRIPTIONS:
                entities.append(VisionAPISensor(coordinator, description, uuid))
            for description in CONSUMPTION_ENTITY_DESCRIPTIONS:
                entities.append(VisionAPISensor(coordinator, description, uuid))
        if coordinator.has_production:
            for description in PRODUCTION_ENTITY_DESCRIPTIONS:
                entities.append(VisionAPISensor(coordinator, description, uuid))
    async_add_entities(entities)
