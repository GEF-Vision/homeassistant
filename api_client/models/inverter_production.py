from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InverterProduction")


@attr.s(auto_attribs=True)
class InverterProduction:
    """
    Attributes:
        today (Union[Unset, int]): Energy transferred since start of today, in watthours (Wh).
        current_week (Union[Unset, int]): Energy transferred since start of this week, in watthours (Wh).
        current_month (Union[Unset, int]): Energy transferred since start of this month, in watthours (Wh).
        current_year (Union[Unset, int]): Energy transferred since start of this year, in watthours (Wh).
        last_24h (Union[Unset, int]): Energy transferred with in last 24 hours, in watthours (Wh).
        last_7d (Union[Unset, int]): Energy transferred with in last 7 days, in watthours (Wh).
        last_31d (Union[Unset, int]): Energy transferred with in last 31 days, in watthours (Wh).
        last_365d (Union[Unset, int]): Energy transferred with in last 365 days, in watthours (Wh).
        lifetime (Union[Unset, int]): Energy transferred during the plant lifetime, in watthours (Wh).
    """

    today: Union[Unset, int] = 0
    current_week: Union[Unset, int] = 0
    current_month: Union[Unset, int] = 0
    current_year: Union[Unset, int] = 0
    last_24h: Union[Unset, int] = 0
    last_7d: Union[Unset, int] = 0
    last_31d: Union[Unset, int] = 0
    last_365d: Union[Unset, int] = 0
    lifetime: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        today = self.today
        current_week = self.current_week
        current_month = self.current_month
        current_year = self.current_year
        last_24h = self.last_24h
        last_7d = self.last_7d
        last_31d = self.last_31d
        last_365d = self.last_365d
        lifetime = self.lifetime

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if today is not UNSET:
            field_dict["today"] = today
        if current_week is not UNSET:
            field_dict["current_week"] = current_week
        if current_month is not UNSET:
            field_dict["current_month"] = current_month
        if current_year is not UNSET:
            field_dict["current_year"] = current_year
        if last_24h is not UNSET:
            field_dict["last_24h"] = last_24h
        if last_7d is not UNSET:
            field_dict["last_7d"] = last_7d
        if last_31d is not UNSET:
            field_dict["last_31d"] = last_31d
        if last_365d is not UNSET:
            field_dict["last_365d"] = last_365d
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        today = d.pop("today", UNSET)

        current_week = d.pop("current_week", UNSET)

        current_month = d.pop("current_month", UNSET)

        current_year = d.pop("current_year", UNSET)

        last_24h = d.pop("last_24h", UNSET)

        last_7d = d.pop("last_7d", UNSET)

        last_31d = d.pop("last_31d", UNSET)

        last_365d = d.pop("last_365d", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        inverter_production = cls(
            today=today,
            current_week=current_week,
            current_month=current_month,
            current_year=current_year,
            last_24h=last_24h,
            last_7d=last_7d,
            last_31d=last_31d,
            last_365d=last_365d,
            lifetime=lifetime,
        )

        inverter_production.additional_properties = d
        return inverter_production

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
