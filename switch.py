import logging
from typing import Any
from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from .entity import EntityDescriptionFactory, VisionAPIEntity
from .const import DOMAIN
from .coordinator import VisionUpdateCoordinator


_LOGGER = logging.getLogger(__name__)


class VisionSwitchEntity(VisionAPIEntity, SwitchEntity):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: SwitchEntityDescription,
        control_id: int | str,
    ):
        super().__init__(coordinator)
        self.control_id = control_id
        self.entity_description = description
        self._attr_unique_id = (
            f"control-{control_id}-{coordinator.uuid}-{description.key}"
        )
        self._attr_name = f"{self.entity_description.name}"
        self.device_identifier = f"plant-{coordinator.uuid}"
        self._device_info = {
            "identifiers": {(DOMAIN, self.device_identifier)},
            "name": self.device_identifier,
            "default_manufacturer": "GEF",
            "default_model": f"Control-{self.control_id}",
        }

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
            description = EntityDescriptionFactory.generate_control_entity_description(
                control
            )
            entities.append(
                VisionSwitchEntity(base.coordinator, description, control.id)
            )
    async_add_entities(entities)
