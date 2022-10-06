import operator
from functools import reduce
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .coordinator import VisionUpdateCoordinator
from .api_client.models import Inverter, Energymeter, Control, Sensor
from .const import (
    CT_SENSOR_ENTITY_DESCRIPTION,
    TEMPERATURE_SENSOR_ENTITY_DESCRIPTION,
    DOMAIN,
    generate_inverter_entity_descriptions,
    generate_energy_entity_descriptions,
    generate_power_entity_descriptions,
    generate_energymeter_entity_descriptions,
    generate_consumption_entity_descriptions,
    generate_grid_interface_entity_descriptions,
    generate_current_sensor_description,
    generate_temperature_sensor_description,
    generate_entity_description,
    VisionSensorEntityDescription,
)
from typing import List

_LOGGER = logging.getLogger(__name__)


class VisionAPISensor(CoordinatorEntity, SensorEntity):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: VisionSensorEntityDescription,
        sensor_id: int | str,
        device_type: str,
        device_model: str | None = None,
    ):
        super().__init__(coordinator)
        self.sensor_id = sensor_id
        self.entity_description = description
        self._attr_unique_id = f"{coordinator.uuid}-{description.key}"
        self._attr_name = f"{self.entity_description.name}"
        self.device_identifier = f"{device_type}-{coordinator.uuid}-{sensor_id}"
        self._device_info = {
            "identifiers": {(DOMAIN, self.device_identifier)},
            "name": self.device_identifier,
            "default_manufacturer": "GEF",
            "default_model": f"APISensor-{self.sensor_id}",
        }
        if device_model:
            self._device_info["model"] = device_model

    @property
    def device_info(self):
        return self._device_info

    def get_value_from_path(self, values, ignore_prefix=False):
        path = self.entity_description.json_path.split("-")
        if ignore_prefix and len(path) > 1:
            path = path[1:]
        return reduce(operator.getitem, path, values)


class VisionSensor(VisionAPISensor):
    @property
    def native_value(self):
        values = self.coordinator.get_sensor_values(self.sensor_id)
        return self.get_value_from_path(values)


class VisionEnergymeterPhaseSensor(VisionAPISensor):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: VisionSensorEntityDescription,
        sensor_id: int | str,
        model_name: str | None,
    ):
        super().__init__(coordinator, description, sensor_id, "meter", model_name)

    @property
    def native_value(self):
        data = self.coordinator.get_energymeter_values(self.sensor_id)
        path, phase = self.entity_description.json_path.split("-")
        for phase_data in data["phase"]:
            if phase_data["phase"] == phase:
                return phase_data[path]
        raise KeyError("Data not found")


class VisionConsumptionSensor(VisionAPISensor):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: VisionSensorEntityDescription,
        sensor_id: int | str,
        model_name: str | None,
    ):
        super().__init__(
            coordinator, description, sensor_id, "consumption", "PlantTotalConsumption"
        )

    @property
    def native_value(self):
        values = self.coordinator.get_energymeter_values("total-consumption")["primary"]
        return self.get_value_from_path(values)


class VisionInverterSensor(VisionAPISensor):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: VisionSensorEntityDescription,
        sensor_id: int | str,
        model_name: str | None,
    ):
        super().__init__(coordinator, description, sensor_id, "inverter", model_name)

    @property
    def native_value(self):
        values = self.coordinator.get_inverter_values(self.sensor_id)
        return self.get_value_from_path(values)


class VisionPlantSensor(VisionAPISensor):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: VisionSensorEntityDescription,
        sensor_id: int | str,
        model_name: str | None,
    ):
        super().__init__(coordinator, description, sensor_id, "plant", model_name)

    @property
    def native_value(self):
        values = self.coordinator.get_total_production()
        return self.get_value_from_path(values)


class VisionEnergymeterPowerSensor(VisionAPISensor):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: VisionSensorEntityDescription,
        sensor_id: int | str,
        model_name: str | None,
    ):
        super().__init__(coordinator, description, sensor_id, "meter", model_name)
        self.direction = description.key.split("-")[-1]

    @property
    def native_value(self):
        values = self.coordinator.get_energymeter_values(self.sensor_id)
        return values["power"][self.direction]


class VisionEnergymeterSensor(VisionAPISensor):
    def __init__(
        self,
        coordinator: VisionUpdateCoordinator,
        description: VisionSensorEntityDescription,
        sensor_id: int | str,
        model_name: str | None,
    ):
        super().__init__(coordinator, description, sensor_id, "meter", model_name)
        self.direction = self.entity_description.key.split("-")[-1]

    @property
    def native_value(self):
        values = self.coordinator.get_energymeter_values(self.sensor_id)
        values = values["energy"][self.direction]
        return self.get_value_from_path(values, True)


class EntityFactory:
    @staticmethod
    def generate_inverter(inverter: Inverter, coordinator: VisionUpdateCoordinator):
        entities = []
        descriptions = generate_inverter_entity_descriptions(inverter.id)
        for description in descriptions:
            entities.append(
                VisionInverterSensor(
                    coordinator, description, inverter.id, inverter.model_name
                )
            )
        return entities

    @staticmethod
    def generate_production(coordinator: VisionUpdateCoordinator):
        entities = []
        descriptions = generate_inverter_entity_descriptions("total")
        for description in descriptions:
            entities.append(
                VisionPlantSensor(
                    coordinator, description, "total", "PlantProductionTotal"
                )
            )
        return entities

    @staticmethod
    def generate_energymeter_entitites(
        coordinator: VisionUpdateCoordinator,
        power_descriptions: List[VisionSensorEntityDescription],
        energy_descriptions: List[VisionSensorEntityDescription],
        phase_descriptions: List[VisionSensorEntityDescription],
        meter_id: int,
        meter_name: str | None = None,
    ):
        entities = []
        if not meter_name:
            meter_name = "Energymeter"
        for description in energy_descriptions:
            entities.append(
                VisionEnergymeterSensor(coordinator, description, meter_id, meter_name)
            )
        for description in power_descriptions:
            entities.append(
                VisionEnergymeterPowerSensor(
                    coordinator, description, meter_id, meter_name
                )
            )
        for description in phase_descriptions:
            entities.append(
                VisionEnergymeterPhaseSensor(
                    coordinator, description, meter_id, meter_name
                )
            )
        return entities

    @staticmethod
    def generate_energymeter(
        coordinator: VisionUpdateCoordinator,
        meter: Energymeter,
        meter_type: str = "consumption",
    ):
        energy, power, phase = generate_energymeter_entity_descriptions(
            meter_type, meter.id
        )
        entities = EntityFactory.generate_energymeter_entitites(
            coordinator, power, energy, phase, meter.id, meter.name
        )
        return entities

    @staticmethod
    def generate_grid_interface(
        coordinator: VisionUpdateCoordinator, meter: Energymeter
    ):
        energy, power, phase = generate_grid_interface_entity_descriptions(meter.id)
        entities = EntityFactory.generate_energymeter_entitites(
            coordinator, power, energy, phase, "grid-interface", "PlantGridInterface"
        )
        return entities

    @staticmethod
    def generate_total_consumption(coordinator: VisionUpdateCoordinator):
        entities = []
        for description in generate_consumption_entity_descriptions():
            entities.append(
                VisionConsumptionSensor(
                    coordinator, description, "consumption", "PlantTotalConsumption"
                )
            )
        return entities

    @staticmethod
    def generate_ct(coordinator: VisionUpdateCoordinator, sensor: Sensor):
        description = generate_current_sensor_description(sensor.id, sensor.name)
        return [VisionSensor(coordinator, description, sensor.id, "CT")]

    @staticmethod
    def generate_temperature(coordinator: VisionUpdateCoordinator, sensor: Sensor):
        description = generate_temperature_sensor_description(sensor.id, sensor.name)
        return [VisionSensor(coordinator, description, sensor.id, "Temperature")]


async def async_setup_entry(hass, entry, async_add_entities) -> None:
    base = hass.data[DOMAIN][entry.entry_id]
    coordinator = base.coordinator
    entities = []
    for inverter in coordinator.inverters:
        # Entitites for each inverter
        entities.extend(EntityFactory.generate_inverter(inverter, coordinator))
    if len(coordinator.inverters) > 1:
        # Entities for total production
        entities.extend(EntityFactory.generate_production(coordinator))
    if coordinator.grid_interface:
        # Entities for grid interface
        entities.extend(
            EntityFactory.generate_grid_interface(
                coordinator, coordinator.grid_interface
            )
        )
    for meter in coordinator.energymeters:
        if meter.meter_type == 1:
            # Entities for consumption meters
            entities.extend(EntityFactory.generate_energymeter(coordinator, meter))
    if coordinator.grid_interface or len(coordinator.consumption_meters) > 0:
        # Entities for total consumption
        entities.extend(EntityFactory.generate_total_consumption(coordinator))
    for sensor in coordinator.sensors:
        if sensor.type == "current":
            # Entities for CT
            entities.extend(EntityFactory.generate_ct(coordinator, sensor))
        elif sensor.type == "temperature":
            # Entities for temperature sensors
            entities.extend(EntityFactory.generate_temperature(coordinator, sensor))
    async_add_entities(entities)
