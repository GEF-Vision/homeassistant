from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.named_power_energy import NamedPowerEnergy
from ..types import UNSET, Unset

T = TypeVar("T", bound="DetailedPowerEnergy")


@attr.s(auto_attribs=True)
class DetailedPowerEnergy:
    """
    Attributes:
        primary (Union[Unset, None, NamedPowerEnergy]):
        detail (Union[Unset, List[NamedPowerEnergy]]):
    """

    primary: Union[Unset, None, NamedPowerEnergy] = UNSET
    detail: Union[Unset, List[NamedPowerEnergy]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.primary, Unset):
            primary = self.primary.to_dict() if self.primary else None

        detail: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = []
            for detail_item_data in self.detail:
                detail_item = detail_item_data.to_dict()

                detail.append(detail_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["primary"] = primary
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _primary = d.pop("primary", UNSET)
        primary: Union[Unset, None, NamedPowerEnergy]
        if _primary is None:
            primary = None
        elif isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = NamedPowerEnergy.from_dict(_primary)

        detail = []
        _detail = d.pop("detail", UNSET)
        for detail_item_data in _detail or []:
            detail_item = NamedPowerEnergy.from_dict(detail_item_data)

            detail.append(detail_item)

        detailed_power_energy = cls(
            primary=primary,
            detail=detail,
        )

        detailed_power_energy.additional_properties = d
        return detailed_power_energy

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
