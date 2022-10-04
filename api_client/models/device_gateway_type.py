from enum import Enum


class DeviceGatewayType(str, Enum):
    READER = "reader"
    ALUSTA = "alusta"

    def __str__(self) -> str:
        return str(self.value)
