import operator
from functools import reduce
import logging
from homeassistant.components.sensor import SensorEntity
from .coordinator import VisionUpdateCoordinator
from .entity import EntityDescriptionFactory, VisionAPIEntity
from .api_client.models import Inverter, Energymeter, Sensor
from .const import (
    DOMAIN,
    VisionSensorEntityDescription,
)

_LOGGER = logging.getLogger(__name__)


class VisionAPISensor(VisionAPIEntity, SensorEntity):
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
        self._attr_unique_id = (
            f"{device_type}-{sensor_id}-{coordinator.uuid}-{description.key}"
        )
        self._attr_name = f"{self.entity_description.name}"
        if device_type == "plant":
            self.device_identifier = f"plant-{coordinator.uuid}"
        else:
            self.device_identifier = f"{device_type}-{sensor_id}-{coordinator.uuid}"
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
    @property
    def native_value(self):
        data = self.coordinator.get_energymeter_values(self.sensor_id)
        path, phase = self.entity_description.json_path.split("-")
        for phase_data in data["phase"]:
            if phase_data["phase"] == phase:
                return phase_data[path]
        raise KeyError("Data not found")


class VisionConsumptionSensor(VisionAPISensor):
    @property
    def native_value(self):
        values = self.coordinator.get_energymeter_values("total-consumption")["primary"]
        return self.get_value_from_path(values)


class VisionProductionSensor(VisionAPISensor):
    @property
    def native_value(self):
        values = self.coordinator.get_inverter_values(self.sensor_id)
        return self.get_value_from_path(values)


class VisionPlantSensor(VisionAPISensor):
    @property
    def native_value(self):
        values = self.coordinator.get_total_production()
        return self.get_value_from_path(values)


class VisionImportExportSensor(VisionAPISensor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Last part of entity description key defines direction (import/export)
        self.direction = self.entity_description.key.split("-")[-1]


class VisionEnergymeterPowerSensor(VisionImportExportSensor):
    @property
    def native_value(self):
        values = self.coordinator.get_energymeter_values(self.sensor_id)
        return values["power"][self.direction]


class VisionEnergymeterSensor(VisionImportExportSensor):
    @property
    def native_value(self):
        values = self.coordinator.get_energymeter_values(self.sensor_id)
        values = values["energy"][self.direction]
        return self.get_value_from_path(values, True)


class SensorFactory:
    @staticmethod
    def create_inverter(coordinator: VisionUpdateCoordinator, inverter: Inverter):
        entities = []
        descriptions = EntityDescriptionFactory.generate_inverter_entity_descriptions(
            inverter
        )
        for desc in descriptions:
            entities.append(
                VisionProductionSensor(
                    coordinator, desc, inverter.id, "inverter", inverter.model_name
                )
            )
        return entities

    @staticmethod
    def create_production(coordinator: VisionUpdateCoordinator):
        entities = []
        descriptions = (
            EntityDescriptionFactory.generate_total_production_entity_descriptions()
        )

        for desc in descriptions:
            entities.append(
                VisionProductionSensor(
                    coordinator,
                    desc,
                    "total-production",
                    "plant",
                    "Power Plant",
                )
            )
        return entities

    @staticmethod
    def create_grid_interface(coordinator: VisionUpdateCoordinator):
        entities = []
        (
            energy,
            power,
            phase,
        ) = EntityDescriptionFactory.generate_grid_interface_entity_descriptions()

        for desc in energy:
            entities.append(
                VisionEnergymeterSensor(
                    coordinator, desc, "grid-interface", "plant", "Power Plant"
                )
            )
        for desc in power:
            entities.append(
                VisionEnergymeterPowerSensor(
                    coordinator, desc, "grid-interface", "plant", "Power Plant"
                )
            )
        for desc in phase:
            entities.append(
                VisionEnergymeterPhaseSensor(
                    coordinator, desc, "grid-interface", "plant", "Power Plant"
                )
            )
        return entities

    @staticmethod
    def create_energymeter(coordinator: VisionUpdateCoordinator, meter: Energymeter):
        entities = []
        (
            energy,
            power,
            phase,
        ) = EntityDescriptionFactory.generate_energymeter_entity_descriptions(meter)

        for desc in energy:
            entities.append(
                VisionEnergymeterSensor(
                    coordinator, desc, meter.id, "meter", meter.name
                )
            )
        for desc in power:
            entities.append(
                VisionEnergymeterPowerSensor(
                    coordinator, desc, meter.id, "meter", meter.name
                )
            )
        for desc in phase:
            entities.append(
                VisionEnergymeterPhaseSensor(
                    coordinator, desc, meter.id, "meter", meter.name
                )
            )
        return entities

    @staticmethod
    def create_total_consumption(coordinator: VisionUpdateCoordinator):
        entities = []
        descriptions = (
            EntityDescriptionFactory.generate_total_consumption_entity_descriptions()
        )

        for desc in descriptions:
            entities.append(
                VisionConsumptionSensor(
                    coordinator, desc, "total-consumption", "plant", "Power Plant"
                )
            )
        return entities

    @staticmethod
    def create_current_sensor(coordinator: VisionUpdateCoordinator, sensor: Sensor):
        desc = EntityDescriptionFactory.generate_ct(sensor)
        return [VisionSensor(coordinator, desc, sensor.id, "current-transformer")]

    @staticmethod
    def create_temperature_sensor(coordinator: VisionUpdateCoordinator, sensor: Sensor):
        desc = EntityDescriptionFactory.generate_temperature(sensor)
        return [VisionSensor(coordinator, desc, sensor.id, "temperature")]


async def async_setup_entry(hass, entry, async_add_entities) -> None:
    base = hass.data[DOMAIN][entry.entry_id]
    coordinator = base.coordinator
    entities = []
    for inverter in coordinator.inverters:
        # Entitites for each inverter
        entities.extend(SensorFactory.create_inverter(coordinator, inverter))

        if len(coordinator.inverters) > 0:
            # Entities for total production
            entities.extend(SensorFactory.create_production(coordinator))
        if coordinator.grid_interface:
            # Entities for grid interface
            entities.extend(SensorFactory.create_grid_interface(coordinator))
        for meter in coordinator.energymeters:
            if meter.meter_type == 1:
                # Entities for consumption meters
                entities.extend(SensorFactory.create_energymeter(coordinator, meter))
        if coordinator.grid_interface or len(coordinator.consumption_meters) > 0:
            # Entities for total consumption
            entities.extend(SensorFactory.create_total_consumption(coordinator))
        for sensor in coordinator.sensors:
            if sensor.sensor_type == "current":
                # Entities for CT
                entities.extend(
                    SensorFactory.create_current_sensor(coordinator, sensor)
                )
            elif sensor.sensor_type == "temperature":
                # Entities for temperature sensors
                entities.extend(
                    SensorFactory.create_temperature_sensor(coordinator, sensor)
                )
    async_add_entities(entities)
