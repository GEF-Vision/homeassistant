"""Constants for the GEF Vision integration."""
from dataclasses import dataclass
from enum import IntEnum
from homeassistant.const import (
    ENERGY_WATT_HOUR,
    POWER_WATT,
    POWER_VOLT_AMPERE_REACTIVE,
    TEMP_CELSIUS,
    ELECTRIC_CURRENT_AMPERE,
    ELECTRIC_POTENTIAL_VOLT,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from typing import List

DOMAIN = "vision"

CLIENT = "client"
DEFAULT_SCAN_INTERVAL = 30
ERROR_SCAN_INTERVAL = 600
VISION_BASE_URL = "https://vision.gef.fi"

VISION_DEVICE_TYPE_INVERTER = "inverter"
VISION_DEVICE_TYPE_ENERGYMETER = "energymeter"
VISION_DEVICE_TYPE_SENSOR = "sensor"
VISION_DEVICE_TYPE_CONTROL = "control"

VISION_METER_TYPE_GRID_INTERFACE = 0
VISION_METER_TYPE_CONSUMPTION = 1


class VisionSensorType(IntEnum):
    VISION_SENSOR_PRODUCTION = 0
    VISION_SENSOR_CONSUMPTION = 1
    VISION_SENSOR_GRID_INTERFACE = 2


@dataclass
class VisionSensorEntityDescription(SensorEntityDescription):
    """Sensor Entity Description for GEF Vision sensors"""

    json_path: str = None


ENERGYMETER_PHASE_ENTITY_DESCRIPTIONS: List[VisionSensorEntityDescription] = [
    VisionSensorEntityDescription(
        json_path="voltage-L1",
        key="voltage_L1",
        name="Voltage L1",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        key="current-L1",
        name="Current L1",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        key="active_power-L1",
        name="Active Power L1",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        key="reactive_power-L1",
        name="Reactive Power L1",
        native_unit_of_measurement=POWER_VOLT_AMPERE_REACTIVE,
        device_class=SensorDeviceClass.POWER,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        key="voltage-L2",
        name="Voltage L2",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        key="current-L2",
        name="Current L2",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        key="active_power-L2",
        name="Active Power L2",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        json_path="reactive_power-L2",
        key="reactive_power_L2",
        name="Reactive Power L2",
        native_unit_of_measurement=POWER_VOLT_AMPERE_REACTIVE,
        device_class=SensorDeviceClass.POWER,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        json_path="voltage-L3",
        key="voltage_L3",
        name="Voltage L3",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        json_path="current-L3",
        key="current_L3",
        name="Current L3",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        json_path="active_power-L3",
        key="active_power_L3",
        name="Active Power L3",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        entity_registry_enabled_default=False,
    ),
    VisionSensorEntityDescription(
        json_path="reactive_power-L3",
        key="reactive_power_L3",
        name="Reactive Power L3",
        native_unit_of_measurement=POWER_VOLT_AMPERE_REACTIVE,
        device_class=SensorDeviceClass.POWER,
        entity_registry_enabled_default=False,
    ),
]
ENERGYMETER_POWER_ENTITY_DESCRIPTIONS: List[VisionSensorEntityDescription] = [
    VisionSensorEntityDescription(
        json_path="power-import",
        key="power-import",
        name="Current import",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    VisionSensorEntityDescription(
        json_path="power-export",
        key="power-export",
        name="Current export",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
]

# Temperature sensor
TEMPERATURE_SENSOR_ENTITY_DESCRIPTION = SensorEntityDescription(
    key="temperature",
    name="Temperature",
    native_unit_of_measurement=TEMP_CELSIUS,
    device_class=SensorDeviceClass.TEMPERATURE,
)

CT_SENSOR_ENTITY_DESCRIPTION = SensorEntityDescription(
    key="current",
    name="Current Transformer",
    native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
    device_class=SensorDeviceClass.CURRENT,
)

energy_keys = [
    "today",
    "current_week",
    "current_month",
    "current_year",
    "last_365d",
    "lifetime",
]

production_power_keys = ["power"]


def generate_entity_description(
    json_path: str,
    key: str,
    name: str,
    native_unit_of_measurement: int,
    device_class: SensorDeviceClass,
    state_class: SensorStateClass = None,
    enabled_by_default=True,
):
    return VisionSensorEntityDescription(
        json_path=json_path,
        key=key,
        name=name,
        native_unit_of_measurement=native_unit_of_measurement,
        device_class=device_class,
        state_class=state_class,
        entity_registry_enabled_default=enabled_by_default,
    )


def generate_energy_entity_descriptions(energy_type: str, suffix: str):
    descriptions = []
    for key in energy_keys:
        name = f"{energy_type.capitalize()}-{key}-{suffix}"
        json_path = f"energy-{key}"
        if key == "lifetime":
            state_class = SensorStateClass.TOTAL_INCREASING
        else:
            state_class = None
        descriptions.append(
            generate_entity_description(
                json_path, name, name, ENERGY_WATT_HOUR, SensorDeviceClass.ENERGY
            )
        )
    return descriptions


def generate_energymeter_power_descriptions(meter_type: str, suffix: str = None):
    descriptions = []
    if suffix:
        keystr = f"{meter_type}-{suffix}-power"
    else:
        keystr = f"{meter_type}-power"
    descriptions.append(
        generate_entity_description(
            "power",
            f"{keystr}-export",
            f"{keystr}-export",
            POWER_WATT,
            SensorDeviceClass.POWER,
        )
    )
    descriptions.append(
        generate_entity_description(
            "power",
            f"{keystr}-import",
            f"{keystr}-import",
            POWER_WATT,
            SensorDeviceClass.POWER,
        )
    )
    return descriptions


def generate_energymeter_phase_descriptions(meter_type: str, suffix: str):
    return [
        VisionSensorEntityDescription(
            json_path="voltage-L1",
            key=f"{meter_type}-voltage-L1-meter-{suffix}",
            name=f"{meter_type.capitalize()}-voltage-L1-meter-{suffix}",
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="current-L1",
            key=f"{meter_type}-current-L1-meter-{suffix}",
            name=f"{meter_type.capitalize()}-current-L1-meter-{suffix}",
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            device_class=SensorDeviceClass.CURRENT,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="active_power-L1",
            key=f"{meter_type}-active_power-L1-meter-{suffix}",
            name=f"{meter_type.capitalize()}-active_power-L1-meter-{suffix}",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="reactive_power-L1",
            key=f"{meter_type}-reactive_power-L1-meter-{suffix}",
            name=f"{meter_type.capitalize()}-reactive_power-L1-meter-{suffix}",
            native_unit_of_measurement=POWER_VOLT_AMPERE_REACTIVE,
            device_class=SensorDeviceClass.POWER,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="voltage-L2",
            key=f"{meter_type}-voltage-L2-meter-{suffix}",
            name=f"{meter_type.capitalize()}-voltage-L2-meter-{suffix}",
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="current-L2",
            key=f"{meter_type}-current-L2-meter-{suffix}",
            name=f"{meter_type.capitalize()}-current-L2-meter-{suffix}",
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            device_class=SensorDeviceClass.CURRENT,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="active_power-L2",
            key=f"{meter_type}-active_power-L2-meter-{suffix}",
            name=f"{meter_type.capitalize()}-active_power-L2-meter-{suffix}",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="reactive_power-L2",
            key=f"{meter_type}-reactive_power-L2-meter-{suffix}",
            name=f"{meter_type.capitalize()}-reactive_power-L2-meter-{suffix}",
            native_unit_of_measurement=POWER_VOLT_AMPERE_REACTIVE,
            device_class=SensorDeviceClass.POWER,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="voltage-L3",
            key=f"{meter_type}-voltage-L3-meter-{suffix}",
            name=f"{meter_type.capitalize()}-voltage-L3-meter-{suffix}",
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="current-L3",
            key=f"{meter_type}-current-L3-meter-{suffix}",
            name=f"{meter_type.capitalize()}-current-L3-meter-{suffix}",
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            device_class=SensorDeviceClass.CURRENT,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="active_power-L3",
            key=f"{meter_type}-active_power-L3-meter-{suffix}",
            name=f"{meter_type.capitalize()}-active_power-L3-meter-{suffix}",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            entity_registry_enabled_default=False,
        ),
        VisionSensorEntityDescription(
            json_path="reactive_power-L3",
            key=f"{meter_type}-reactive_power-L3-meter-{suffix}",
            name=f"{meter_type.capitalize()}-reactive_power-L3-meter-{suffix}",
            native_unit_of_measurement=POWER_VOLT_AMPERE_REACTIVE,
            device_class=SensorDeviceClass.POWER,
            entity_registry_enabled_default=False,
        ),
    ]


def generate_power_entity_descriptions(energy_type: str, suffix: str):
    return [
        VisionSensorEntityDescription(
            json_path="power",
            key=f"{energy_type}-power-now-{suffix}",
            name=f"{energy_type.capitalize()} now {suffix}",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
        ),
    ]


def generate_inverter_entity_descriptions(dev_id: int):
    suffix = f"inverter-{dev_id}"
    entities = generate_energy_entity_descriptions("production", suffix)
    entities.extend(generate_power_entity_descriptions("production", suffix))
    return entities


def generate_consumption_entity_descriptions():
    suffix = f"total"
    entities = generate_energy_entity_descriptions("consumption", suffix)
    entities.extend(generate_power_entity_descriptions("consumption", suffix))
    return entities


def generate_grid_interface_entity_descriptions(dev_id: int):
    energy = generate_energy_entity_descriptions("grid-interface", "import")
    energy.extend(generate_energy_entity_descriptions("grid-interface", "export"))
    power = generate_energymeter_power_descriptions("grid-interface", dev_id)
    phase = generate_energymeter_phase_descriptions("grid-interface", dev_id)
    return energy, power, phase


def generate_energymeter_entity_descriptions(meter_type: str, suffix: str):
    energy = generate_energy_entity_descriptions(meter_type, f"{suffix}-import")
    energy.extend(generate_energy_entity_descriptions(meter_type, f"{suffix}-export"))
    power = generate_energymeter_power_descriptions(meter_type, suffix)
    phase = generate_energymeter_phase_descriptions(meter_type, suffix)
    return energy, power, phase


def generate_current_sensor_description(sensor_id: int, sensor_name: str | None):
    if sensor_name:
        keystr = f"temperature-{sensor_name}-{sensor_id}"
    else:
        keystr = f"temperature-{sensor_id}"
    return generate_entity_description(
        "value",
        keystr,
        keystr.capitalize().replace("-", " "),
        ELECTRIC_CURRENT_AMPERE,
        SensorDeviceClass.CURRENT,
    )


def generate_temperature_sensor_description(sensor_id: int, sensor_name: str | None):
    if sensor_name:
        keystr = f"temperature-{sensor_name}-{sensor_id}"
    else:
        keystr = f"temperature-{sensor_id}"
    return generate_entity_description(
        "value",
        keystr,
        keystr.capitalize().replace("-", " "),
        TEMP_CELSIUS,
        SensorDeviceClass.TEMPERATURE,
    )
