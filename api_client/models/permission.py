from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Permission")


@attr.s(auto_attribs=True)
class Permission:
    """
    Attributes:
        change_settings (Union[Unset, bool]): Required for altering settings of the plant and devices connected to it.
        change_control_state (Union[Unset, bool]): Required for changing the state of controlled loads.
        view_consumption (Union[Unset, bool]): Required for viewing consumption and grid interface measurements.
        restart_device (Union[Unset, bool]): Required for restarting devices connected to the plant.
    """

    change_settings: Union[Unset, bool] = False
    change_control_state: Union[Unset, bool] = False
    view_consumption: Union[Unset, bool] = False
    restart_device: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        change_settings = self.change_settings
        change_control_state = self.change_control_state
        view_consumption = self.view_consumption
        restart_device = self.restart_device

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_settings is not UNSET:
            field_dict["change_settings"] = change_settings
        if change_control_state is not UNSET:
            field_dict["change_control_state"] = change_control_state
        if view_consumption is not UNSET:
            field_dict["view_consumption"] = view_consumption
        if restart_device is not UNSET:
            field_dict["restart_device"] = restart_device

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        change_settings = d.pop("change_settings", UNSET)

        change_control_state = d.pop("change_control_state", UNSET)

        view_consumption = d.pop("view_consumption", UNSET)

        restart_device = d.pop("restart_device", UNSET)

        permission = cls(
            change_settings=change_settings,
            change_control_state=change_control_state,
            view_consumption=view_consumption,
            restart_device=restart_device,
        )

        permission.additional_properties = d
        return permission

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
