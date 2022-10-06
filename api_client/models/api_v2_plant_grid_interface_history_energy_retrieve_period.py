from enum import Enum


class ApiV2PlantGridInterfaceHistoryEnergyRetrievePeriod(str, Enum):
    VALUE_0 = "1h"
    VALUE_1 = "2h"
    VALUE_2 = "3h"
    VALUE_3 = "4h"
    VALUE_4 = "6h"
    VALUE_5 = "12h"
    VALUE_6 = "24h"

    def __str__(self) -> str:
        return str(self.value)
