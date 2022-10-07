"""Constants for the GEF Vision integration."""
from dataclasses import dataclass
from enum import IntEnum
from typing import List
from homeassistant.const import (
    POWER_WATT,
    POWER_VOLT_AMPERE_REACTIVE,
    TEMP_CELSIUS,
    ELECTRIC_CURRENT_AMPERE,
    ELECTRIC_POTENTIAL_VOLT,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
)

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


PHASE_KEY_TO_UNIT = {
    "voltage": ELECTRIC_POTENTIAL_VOLT,
    "current": ELECTRIC_CURRENT_AMPERE,
    "active_power": POWER_WATT,
    "reactive_power": POWER_VOLT_AMPERE_REACTIVE,
}

PHASE_KEY_TO_SENSOR_CLASS = {
    "voltage": SensorDeviceClass.VOLTAGE,
    "current": SensorDeviceClass.CURRENT,
    "active_power": SensorDeviceClass.POWER,
    "reactive_power": SensorDeviceClass.POWER,
}

PHASE_KEYS = ["voltage", "current", "active_power", "reactive_power"]
PHASE_IDS = ["L1", "L2", "L3"]

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

ENERGY_KEYS = [
    "today",
    "current_week",
    "current_month",
    "current_year",
    "last_365d",
    "lifetime",
]

production_power_keys = ["power"]
