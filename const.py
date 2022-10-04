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
DEFAULT_SCAN_INTERVAL = 30
VISION_BASE_URL = "https://vision.gef.fi"


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
        key="production-week",
        json_key="production",
        json_path="energy-current_week",
        name="Production this week",
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
        key="production-year",
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
        name="Produced energy total",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    VisionSensorEntityDescription(
        key="production-365d",
        json_key="production",
        json_path="energy-last_365d",
        name="Produced energy last 365 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="production-now",
        json_key="production",
        json_path="power",
        name="Production now",
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
        name="Consumption now",
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
        key="consumption-week",
        json_key="consumption",
        json_path="energy-current_week",
        name="Consumption this week",
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
        key="consumption-365d",
        json_key="consumption",
        json_path="energy-last_365d",
        name="Consumption last 365 days",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
    ),
    VisionSensorEntityDescription(
        key="consumption-lifetime",
        json_key="consumption",
        json_path="energy-lifetime",
        name="Consumed energy total",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
]

GRID_INTERFACE_ENTITY_DESCRIPTIONS: list[VisionSensorEntityDescription] = [
    # Import
    VisionSensorEntityDescription(
        key="power-import-now",
        json_key="grid_interface",
        json_path="power-import",
        name="Import power",
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
        key="energy-import-week",
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
        name="Imported energy total",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    # Export
    VisionSensorEntityDescription(
        key="power-export-now",
        json_key="grid_interface",
        json_path="power-export",
        name="Export power",
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
        key="energy-export-current_week",
        json_key="grid_interface",
        json_path="energy-export-current_week",
        name="Exported energy this week",
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
        name="Exported energy total",
        native_unit_of_measurement=ENERGY_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
]
