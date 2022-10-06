from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN
from typing import Any
import logging


_LOGGER = logging.getLogger(__name__)


class VisionSwitchEntity(CoordinatorEntity, SwitchEntity):
    def __init__(
        self, coordinator: Any, description: SwitchEntityDescription, control_id: int
    ):
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{coordinator.uuid}-control-{control_id}"
        self._attr_name = f"control-{control_id}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.uuid)},
            manufacturer="GreenEnergy Finland Oy",
            name=coordinator.name,
        )
        self.control_id = control_id

    @property
    def available(self) -> bool:
        return self.coordinator.get_control(self.control_id).get("active", False)

    @property
    def is_on(self) -> bool:
        return (
            True
            if self.coordinator.get_control(self.control_id)["output_state"] == 2
            else False
        )

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self.coordinator.set_control_state(self.control_id, False)

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self.coordinator.set_control_state(self.control_id, True)


async def async_setup_entry(hass, entry, async_add_entities) -> None:
    base = hass.data[DOMAIN][entry.entry_id]
    entities = []
    if base.coordinator.controls:
        for control in base.coordinator.controls:
            if control.name:
                keystr = f"control-{control.name}-{control.id}"
            else:
                keystr = f"control-{control.id}"
            description = SwitchEntityDescription(
                key=keystr, name=keystr.capitalize().replace("-", " ")
            )
            entities.append(
                VisionSwitchEntity(base.coordinator, description, control.id)
            )
    async_add_entities(entities)
