from enum import Enum


class ApiV2PlantDeviceSensorHistoryRetrievePeriod(str, Enum):
    VALUE_0 = "1m"
    VALUE_1 = "5m"
    VALUE_2 = "15m"
    VALUE_3 = "30m"
    VALUE_4 = "1h"
    VALUE_5 = "2h"
    VALUE_6 = "3h"
    VALUE_7 = "4h"
    VALUE_8 = "6h"
    VALUE_9 = "12h"
    VALUE_10 = "24h"

    def __str__(self) -> str:
        return str(self.value)
