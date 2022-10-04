import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.history_device_series import HistoryDeviceSeries
from ..models.history_response_period import HistoryResponsePeriod
from ..models.history_response_response_format import HistoryResponseResponseFormat
from ..models.history_series import HistorySeries
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoryResponse")


@attr.s(auto_attribs=True)
class HistoryResponse:
    """
    Attributes:
        detail (List[HistoryDeviceSeries]): List of detailed series, allowing more detailed presentation if required.
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        period (Union[Unset, HistoryResponsePeriod]):  Default: HistoryResponsePeriod.VALUE_1.
        format_ (Union[Unset, HistoryResponseResponseFormat]):  Default: HistoryResponseResponseFormat.JSON.
        unit (Union[Unset, str]):  Default: ''.
        primary (Optional[HistorySeries]):
    """

    detail: List[HistoryDeviceSeries]
    primary: Optional[HistorySeries]
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    period: Union[Unset, HistoryResponsePeriod] = HistoryResponsePeriod.VALUE_1
    format_: Union[Unset, HistoryResponseResponseFormat] = HistoryResponseResponseFormat.JSON
    unit: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        detail = []
        for detail_item_data in self.detail:
            detail_item = detail_item_data.to_dict()

            detail.append(detail_item)

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        period: Union[Unset, str] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.value

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        unit = self.unit
        primary = self.primary.to_dict() if self.primary else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
                "primary": primary,
            }
        )
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if period is not UNSET:
            field_dict["period"] = period
        if format_ is not UNSET:
            field_dict["format"] = format_
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        detail = []
        _detail = d.pop("detail")
        for detail_item_data in _detail:
            detail_item = HistoryDeviceSeries.from_dict(detail_item_data)

            detail.append(detail_item)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.datetime]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        _period = d.pop("period", UNSET)
        period: Union[Unset, HistoryResponsePeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = HistoryResponsePeriod(_period)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, HistoryResponseResponseFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = HistoryResponseResponseFormat(_format_)

        unit = d.pop("unit", UNSET)

        _primary = d.pop("primary")
        primary: Optional[HistorySeries]
        if _primary is None:
            primary = None
        else:
            primary = HistorySeries.from_dict(_primary)

        history_response = cls(
            detail=detail,
            start=start,
            end=end,
            period=period,
            format_=format_,
            unit=unit,
            primary=primary,
        )

        history_response.additional_properties = d
        return history_response

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
