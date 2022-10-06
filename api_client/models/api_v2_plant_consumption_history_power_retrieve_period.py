from enum import Enum


class ApiV2PlantConsumptionHistoryPowerRetrievePeriod(str, Enum):
    VALUE_0 = "1m"
    VALUE_1 = "5m"
    VALUE_2 = "15m"
    VALUE_3 = "30m"
    VALUE_4 = "1h"

    def __str__(self) -> str:
        return str(self.value)
