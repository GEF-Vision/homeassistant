from enum import Enum


class ApiV2PlantGridInterfaceHistoryEnergyRetrieveResponseFormat(str, Enum):
    JSON = "json"
    CSV = "csv"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)
