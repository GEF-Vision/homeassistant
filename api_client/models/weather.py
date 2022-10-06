from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.weather_point import WeatherPoint

T = TypeVar("T", bound="Weather")


@attr.s(auto_attribs=True)
class Weather:
    """
    Attributes:
        current (WeatherPoint):
        forecast (List[WeatherPoint]): Weather conditions for next 5 days for the plant
    """

    current: WeatherPoint
    forecast: List[WeatherPoint]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current = self.current.to_dict()

        forecast = []
        for forecast_item_data in self.forecast:
            forecast_item = forecast_item_data.to_dict()

            forecast.append(forecast_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "forecast": forecast,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current = WeatherPoint.from_dict(d.pop("current"))

        forecast = []
        _forecast = d.pop("forecast")
        for forecast_item_data in _forecast:
            forecast_item = WeatherPoint.from_dict(forecast_item_data)

            forecast.append(forecast_item)

        weather = cls(
            current=current,
            forecast=forecast,
        )

        weather.additional_properties = d
        return weather

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
