from enum import Enum


class GatewayGatewayType(str, Enum):
    READER = "reader"
    ALUSTA = "alusta"

    def __str__(self) -> str:
        return str(self.value)
