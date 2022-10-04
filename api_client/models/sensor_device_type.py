from enum import Enum


class SensorDeviceType(str, Enum):
    UNKNOWN = "unknown"
    INVERTER = "inverter"
    CONTROL = "control"
    ENERGYMETER = "energymeter"
    AIR_TO_AIR_HEATPUMP = "air-to-air-heatpump"
    SENSOR = "sensor"

    def __str__(self) -> str:
        return str(self.value)
