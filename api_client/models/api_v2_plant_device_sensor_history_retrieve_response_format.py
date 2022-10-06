from enum import Enum


class ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat(str, Enum):
    JSON = "json"
    CSV = "csv"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)
