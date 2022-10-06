import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WeatherPoint")


@attr.s(auto_attribs=True)
class WeatherPoint:
    """
    Attributes:
        time (Union[Unset, None, datetime.datetime]): Timestamp for the weather information
        temperature (Union[Unset, None, float]): Temperature in Celsius (°C)
        pressure (Union[Unset, None, int]): Pressure in hectopascals (hPa)
        humidity (Union[Unset, None, int]): Humidity in percent (%)
        cloud_coverage (Union[Unset, None, int]): Cloud coverage in percent (%)
        wind_speed (Union[Unset, None, float]): Wind speed in meters per second (m/s)
        wind_direction (Union[Unset, None, int]): Wind direction in degrees (°)
        icon (Union[Unset, None, str]): Weather icon as specified by OpenWeatherMap
        icon_id (Union[Unset, None, int]): Weather icon ID as specified by OpenWeatherMap
    """

    time: Union[Unset, None, datetime.datetime] = UNSET
    temperature: Union[Unset, None, float] = UNSET
    pressure: Union[Unset, None, int] = UNSET
    humidity: Union[Unset, None, int] = UNSET
    cloud_coverage: Union[Unset, None, int] = UNSET
    wind_speed: Union[Unset, None, float] = UNSET
    wind_direction: Union[Unset, None, int] = UNSET
    icon: Union[Unset, None, str] = UNSET
    icon_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time: Union[Unset, None, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat() if self.time else None

        temperature = self.temperature
        pressure = self.pressure
        humidity = self.humidity
        cloud_coverage = self.cloud_coverage
        wind_speed = self.wind_speed
        wind_direction = self.wind_direction
        icon = self.icon
        icon_id = self.icon_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if pressure is not UNSET:
            field_dict["pressure"] = pressure
        if humidity is not UNSET:
            field_dict["humidity"] = humidity
        if cloud_coverage is not UNSET:
            field_dict["cloud_coverage"] = cloud_coverage
        if wind_speed is not UNSET:
            field_dict["wind_speed"] = wind_speed
        if wind_direction is not UNSET:
            field_dict["wind_direction"] = wind_direction
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_id is not UNSET:
            field_dict["icon_id"] = icon_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _time = d.pop("time", UNSET)
        time: Union[Unset, None, datetime.datetime]
        if _time is None:
            time = None
        elif isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        temperature = d.pop("temperature", UNSET)

        pressure = d.pop("pressure", UNSET)

        humidity = d.pop("humidity", UNSET)

        cloud_coverage = d.pop("cloud_coverage", UNSET)

        wind_speed = d.pop("wind_speed", UNSET)

        wind_direction = d.pop("wind_direction", UNSET)

        icon = d.pop("icon", UNSET)

        icon_id = d.pop("icon_id", UNSET)

        weather_point = cls(
            time=time,
            temperature=temperature,
            pressure=pressure,
            humidity=humidity,
            cloud_coverage=cloud_coverage,
            wind_speed=wind_speed,
            wind_direction=wind_direction,
            icon=icon,
            icon_id=icon_id,
        )

        weather_point.additional_properties = d
        return weather_point

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
