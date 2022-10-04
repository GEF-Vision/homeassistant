from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.history_extra import HistoryExtra
from ..models.history_point import HistoryPoint
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoryDeviceSeries")


@attr.s(auto_attribs=True)
class HistoryDeviceSeries:
    """
    Attributes:
        name (str):
        data (List[HistoryPoint]):
        extra (Union[Unset, None, HistoryExtra]):
        pk (Union[Unset, None, int]): Primary key of the device, if series links directly to a device.
    """

    name: str
    data: List[HistoryPoint]
    extra: Union[Unset, None, HistoryExtra] = UNSET
    pk: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        extra: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict() if self.extra else None

        pk = self.pk

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "data": data,
            }
        )
        if extra is not UNSET:
            field_dict["extra"] = extra
        if pk is not UNSET:
            field_dict["pk"] = pk

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = HistoryPoint.from_dict(data_item_data)

            data.append(data_item)

        _extra = d.pop("extra", UNSET)
        extra: Union[Unset, None, HistoryExtra]
        if _extra is None:
            extra = None
        elif isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = HistoryExtra.from_dict(_extra)

        pk = d.pop("pk", UNSET)

        history_device_series = cls(
            name=name,
            data=data,
            extra=extra,
            pk=pk,
        )

        history_device_series.additional_properties = d
        return history_device_series

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
