from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.components.switch import SwitchEntityDescription
from homeassistant.const import (
    ENERGY_WATT_HOUR,
    POWER_WATT,
    ELECTRIC_CURRENT_AMPERE,
    TEMP_CELSIUS,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import (
    ENERGY_KEYS,
    PHASE_KEYS,
    PHASE_IDS,
    PHASE_KEY_TO_SENSOR_CLASS,
    PHASE_KEY_TO_UNIT,
    VisionSensorEntityDescription,
)
from .api_client.models import Inverter, Energymeter, Control, Sensor
from .coordinator import VisionUpdateCoordinator


class VisionAPIEntity(CoordinatorEntity):
    def __init__(self, coordinator: VisionUpdateCoordinator):
        super().__init__(coordinator)


class EntityDescriptionFactory:
    @staticmethod
    def generate_sensor_entity_description(
        json_path: str,
        key: str,
        native_unit_of_measurement: int,
        device_class: SensorDeviceClass,
        state_class: SensorStateClass = None,
        enabled_by_default=True,
    ):
        return VisionSensorEntityDescription(
            json_path=json_path,
            key=key,
            name=key.capitalize().replace("-", " "),
            native_unit_of_measurement=native_unit_of_measurement,
            device_class=device_class,
            state_class=state_class,
            entity_registry_enabled_default=enabled_by_default,
        )

    @staticmethod
    def generate_keystr(
        prefix: str, suffix: str, key: str, sensor_id: int | str = None
    ):
        if sensor_id:
            return f"{prefix}-{sensor_id}-{key}-{suffix}"
        return f"{prefix}-{key}-{suffix}"

    @staticmethod
    def generate_energy_entity_descriptions(
        prefix: str, suffix: str, sensor_id: int | str = None
    ):
        descriptions = []
        for key in ENERGY_KEYS:
            keystr = EntityDescriptionFactory.generate_keystr(
                prefix, suffix, key, sensor_id
            )
            json_path = f"energy-{key}"
            if key == "lifetime":
                state_class = SensorStateClass.TOTAL_INCREASING
            else:
                state_class = None
            descriptions.append(
                EntityDescriptionFactory.generate_sensor_entity_description(
                    json_path,
                    keystr,
                    ENERGY_WATT_HOUR,
                    SensorDeviceClass.ENERGY,
                    state_class,
                )
            )

        return descriptions

    @staticmethod
    def generate_inverter_entity_descriptions(inverter: Inverter):
        descriptions = EntityDescriptionFactory.generate_energy_entity_descriptions(
            "inverter", "production", inverter.id
        )
        power_key = EntityDescriptionFactory.generate_keystr(
            "inverter", "production", "power-now", inverter.id
        )
        descriptions.append(
            EntityDescriptionFactory.generate_sensor_entity_description(
                "power", power_key, POWER_WATT, SensorDeviceClass.POWER
            )
        )
        return descriptions

    @staticmethod
    def generate_total_production_entity_descriptions():
        descriptions = EntityDescriptionFactory.generate_energy_entity_descriptions(
            "plant", "production", "total"
        )
        power_key = EntityDescriptionFactory.generate_keystr(
            "plant", "production", "power-now", "total"
        )
        descriptions.append(
            EntityDescriptionFactory.generate_sensor_entity_description(
                "power", power_key, POWER_WATT, SensorDeviceClass.POWER
            )
        )
        return descriptions

    @staticmethod
    def generate_total_consumption_entity_descriptions():
        descriptions = EntityDescriptionFactory.generate_energy_entity_descriptions(
            "plant", "consumption", "total"
        )
        power_key = EntityDescriptionFactory.generate_keystr(
            "plant", "consumption", "power-now", "total"
        )
        descriptions.append(
            EntityDescriptionFactory.generate_sensor_entity_description(
                "power", power_key, POWER_WATT, SensorDeviceClass.POWER
            )
        )
        return descriptions

    @staticmethod
    def generate_phase_entity_descriptions(prefix: str, suffix: str):
        descriptions = []
        for phase in PHASE_IDS:
            for key in PHASE_KEYS:
                keystr = EntityDescriptionFactory.generate_keystr(
                    prefix, suffix, f"{key}-{phase}"
                )
                descriptions.append(
                    EntityDescriptionFactory.generate_sensor_entity_description(
                        f"{key}-{phase}",
                        keystr,
                        PHASE_KEY_TO_UNIT[key],
                        PHASE_KEY_TO_SENSOR_CLASS[key],
                    )
                )
        return descriptions

    @staticmethod
    def generate_grid_interface_entity_descriptions():
        energy = EntityDescriptionFactory.generate_energy_entity_descriptions(
            "plant",
            "export",
            "grid-interface",
        )
        energy.extend(
            EntityDescriptionFactory.generate_energy_entity_descriptions(
                "plant", "import", "grid-interface"
            )
        )
        power_export_key = EntityDescriptionFactory.generate_keystr(
            "plant", "current-export", "grid-interface"
        )
        power_import_key = EntityDescriptionFactory.generate_keystr(
            "plant", "current-import", "grid-interface"
        )
        power = [
            EntityDescriptionFactory.generate_sensor_entity_description(
                "power-export", power_export_key, POWER_WATT, SensorDeviceClass.POWER
            ),
            EntityDescriptionFactory.generate_sensor_entity_description(
                "power-import", power_import_key, POWER_WATT, SensorDeviceClass.POWER
            ),
        ]
        phase = EntityDescriptionFactory.generate_phase_entity_descriptions(
            "plant", "grid-interface"
        )
        return energy, power, phase

    @staticmethod
    def generate_control_entity_description(control: Control):
        if control.name:
            keystr = f"control-{control.name}"
        else:
            keystr = f"control-{control.id}"
        return SwitchEntityDescription(
            key=keystr, name=keystr.capitalize().replace("-", " ")
        )

    @staticmethod
    def generate_energymeter_entity_descriptions(meter: Energymeter):
        energy = EntityDescriptionFactory.generate_energy_entity_descriptions(
            "meter", "export", meter.id
        )
        energy.extend(
            EntityDescriptionFactory.generate_energy_entity_descriptions(
                "meter", "import", meter.id
            )
        )
        power_export_key = EntityDescriptionFactory.generate_keystr(
            "meter", "current-export", meter.id
        )
        power_import_key = EntityDescriptionFactory.generate_keystr(
            "meter", "current-import", meter.id
        )
        power = [
            EntityDescriptionFactory.generate_sensor_entity_description(
                "power-export", power_export_key, POWER_WATT, SensorDeviceClass.POWER
            ),
            EntityDescriptionFactory.generate_sensor_entity_description(
                "power-import", power_import_key, POWER_WATT, SensorDeviceClass.POWER
            ),
        ]
        phase = EntityDescriptionFactory.generate_phase_entity_descriptions(
            "meter", meter.id
        )
        return energy, power, phase

    @staticmethod
    def generate_ct(sensor: Sensor):
        return EntityDescriptionFactory.generate_sensor_entity_description(
            "value",
            f"current_transformer-{sensor.id}",
            ELECTRIC_CURRENT_AMPERE,
            SensorDeviceClass.CURRENT,
        )

    @staticmethod
    def generate_temperature(sensor: Sensor):
        return EntityDescriptionFactory.generate_sensor_entity_description(
            "value",
            f"temperature-{sensor.id}",
            TEMP_CELSIUS,
            SensorDeviceClass.CURRENT,
        )
