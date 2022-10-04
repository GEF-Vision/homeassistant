from enum import Enum


class SensorSensorType(str, Enum):
    TEMPERATURE = "temperature"
    CURRENT = "current"

    def __str__(self) -> str:
        return str(self.value)
