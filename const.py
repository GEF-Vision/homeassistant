"""Constants for the GEF Vision integration."""

from dataclasses import dataclass
from homeassistant.const import ENERGY_WATT_HOUR, POWER_WATT
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)

DOMAIN = "vision"

CLIENT = "client"
HAS_ENERGYMETER = "has_energymeter"
HAS_INVERTER = "has_inverter"
POLL_INTERVAL = 30


@dataclass
class VisionSensorEntityDescription(SensorEntityDescription):
    """Sensor Entity Description for GEF Vision sensors"""

    json_key: str = None
    json_path: str = None


PRODUCTION_ENTITY_DESCRIPTIONS: list[VisionSensorEntityDescription] = [
    VisionSensorEntityDescription(
        key="production-today",
        json_key="production",
        json_path="energy-today",
        name="Production today",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-month",
        json_key="production",
        json_path="energy-current_month",
        name="Production this month",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-current_year",
        json_key="production",
        json_path="energy-current_year",
        name="Production this year",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-lifetime",
        json_key="production",
        json_path="energy-lifetime",
        name="Total produced energy",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    VisionSensorEntityDescription(
        key="production-last_24h",
        json_key="production",
        json_path="energy-last_24h",
        name="Production last 24 hours",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-last_7d",
        json_key="production",
        json_path="energy-last_7d",
        name="Production last 7 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-last_31d",
        json_key="production",
        json_path="energy-last_31d",
        name="Production last 31 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-last_365d",
        json_key="production",
        json_path="energy-last_365d",
        name="Production last 365 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-now",
        json_key="production",
        json_path="power",
        name="Current production",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
]

CONSUMPTION_ENTITY_DESCRIPTIONS: list[VisionSensorEntityDescription] = [
    VisionSensorEntityDescription(
        key="consumption-now",
        json_key="consumption",
        json_path="power",
        name="Current consumption",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    VisionSensorEntityDescription(
        key="consumption-today",
        json_key="consumption",
        json_path="energy-today",
        name="Consumption today",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="consumption-month",
        json_key="consumption",
        json_path="energy-current_month",
        name="Consumption this month",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="consumption-year",
        json_key="consumption",
        json_path="energy-current_year",
        name="Consumption this year",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="consumption-lifetime",
        json_key="consumption",
        json_path="energy-lifetime",
        name="Total consumed energy",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    VisionSensorEntityDescription(
        key="consumption-last_24h",
        json_key="consumption",
        json_path="energy-last_24h",
        name="Consumption last 24 hours",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="consumption-last_7d",
        json_key="consumption",
        json_path="energy-last_7d",
        name="Consumption last 7 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="consumption-last_31d",
        json_key="consumption",
        json_path="energy-last_31d",
        name="Consumption last 31 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="consumption-last_365d",
        json_key="consumption",
        json_path="energy-last_365d",
        name="Consumption last 365 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
]

GRID_INTERFACE_ENTITY_DESCRIPTIONS: list[VisionSensorEntityDescription] = [
    # Import
    VisionSensorEntityDescription(
        key="power-import-now",
        json_key="grid_interface",
        json_path="power-import",
        name="Current import power",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    VisionSensorEntityDescription(
        key="energy-import-today",
        json_key="grid_interface",
        json_path="energy-import-today",
        name="Imported energy today",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-import-current_week",
        json_key="grid_interface",
        json_path="energy-import-current_week",
        name="Imported energy this week",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-import-current_month",
        json_key="grid_interface",
        json_path="energy-import-current_month",
        name="Imported energy this month",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-import-current_year",
        json_key="grid_interface",
        json_path="energy-import-current_year",
        name="Imported energy this year",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-import-last_24h",
        json_key="grid_interface",
        json_path="energy-import-last_24h",
        name="Imported energy last 24 hours",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-import-last_7d",
        json_key="grid_interface",
        json_path="energy-import-last_7d",
        name="Imported energy last 7 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-import-last_365d",
        json_key="grid_interface",
        json_path="energy-import-last_365d",
        name="Imported energy last 365 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-import-lifetime",
        json_key="grid_interface",
        json_path="energy-import-lifetime",
        name="Total imported energy",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    # Export
    VisionSensorEntityDescription(
        key="power-export-now",
        json_key="grid_interface",
        json_path="power-export",
        name="Current export power",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    VisionSensorEntityDescription(
        key="energy-export-today",
        json_key="grid_interface",
        json_path="energy-export-today",
        name="Exported energy today",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-export-current_month",
        json_key="grid_interface",
        json_path="energy-export-current_month",
        name="Exported energy this month",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-export-current_year",
        json_key="grid_interface",
        json_path="energy-export-current_year",
        name="Exported energy this year",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-export-last_24h",
        json_key="grid_interface",
        json_path="energy-export-last_24h",
        name="Exported energy last 24 hours",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-export-last_7d",
        json_key="grid_interface",
        json_path="energy-export-last_7d",
        name="Exported energy last 7 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-export-last_365d",
        json_key="grid_interface",
        json_path="energy-export-last_365d",
        name="Exported energy last 365 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="energy-export-lifetime",
        json_key="grid_interface",
        json_path="energy-export-lifetime",
        name="Total exported energy",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
]
