import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.override_status import OverrideStatus
from ..models.patched_control_device_type import PatchedControlDeviceType
from ..models.patched_control_output_state import PatchedControlOutputState
from ..models.patched_control_state import PatchedControlState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedControl")


@attr.s(auto_attribs=True)
class PatchedControl:
    """
    Attributes:
        gateway (Union[Unset, DeviceGateway]):
        device_type (Union[Unset, PatchedControlDeviceType]): Device type
        id (Union[Unset, int]): Unique (per device-type) identifier of the device.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
        state (Union[Unset, PatchedControlState]): State of the device. Possible choices are:<br> 0: Error<br> 1:
            Warning<br> 2: OK<br>
        commission_date (Union[Unset, datetime.date]): Date when the device was commissioned.
        active (Union[Unset, bool]): Is the device active? Devices can become inactive for example when exchanged to a
            new one.
        last_update (Union[Unset, datetime.datetime]): Time of last update for device measurements.
        output_state (Union[Unset, PatchedControlOutputState]): Output state of the control device. Possible choices
            are:<br> 0: Unknown<br> 1: Off<br> 2: On<br>
        controlled_load_power (Union[Unset, int]): Nominal power of the controlled load in watts (W).
        override (Union[Unset, OverrideStatus]):
    """

    gateway: Union[Unset, DeviceGateway] = UNSET
    device_type: Union[Unset, PatchedControlDeviceType] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = ""
    state: Union[Unset, PatchedControlState] = UNSET
    commission_date: Union[Unset, datetime.date] = UNSET
    active: Union[Unset, bool] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    output_state: Union[Unset, PatchedControlOutputState] = UNSET
    controlled_load_power: Union[Unset, int] = UNSET
    override: Union[Unset, OverrideStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.to_dict()

        device_type: Union[Unset, str] = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type.value

        id = self.id
        name = self.name
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        commission_date: Union[Unset, str] = UNSET
        if not isinstance(self.commission_date, Unset):
            commission_date = self.commission_date.isoformat()

        active = self.active
        last_update: Union[Unset, str] = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

        output_state: Union[Unset, int] = UNSET
        if not isinstance(self.output_state, Unset):
            output_state = self.output_state.value

        controlled_load_power = self.controlled_load_power
        override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.override, Unset):
            override = self.override.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if commission_date is not UNSET:
            field_dict["commission_date"] = commission_date
        if active is not UNSET:
            field_dict["active"] = active
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if output_state is not UNSET:
            field_dict["output_state"] = output_state
        if controlled_load_power is not UNSET:
            field_dict["controlled_load_power"] = controlled_load_power
        if override is not UNSET:
            field_dict["override"] = override

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _gateway = d.pop("gateway", UNSET)
        gateway: Union[Unset, DeviceGateway]
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = DeviceGateway.from_dict(_gateway)

        _device_type = d.pop("device_type", UNSET)
        device_type: Union[Unset, PatchedControlDeviceType]
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = PatchedControlDeviceType(_device_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PatchedControlState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PatchedControlState(_state)

        _commission_date = d.pop("commission_date", UNSET)
        commission_date: Union[Unset, datetime.date]
        if isinstance(_commission_date, Unset):
            commission_date = UNSET
        else:
            commission_date = isoparse(_commission_date).date()

        active = d.pop("active", UNSET)

        _last_update = d.pop("last_update", UNSET)
        last_update: Union[Unset, datetime.datetime]
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update)

        _output_state = d.pop("output_state", UNSET)
        output_state: Union[Unset, PatchedControlOutputState]
        if isinstance(_output_state, Unset):
            output_state = UNSET
        else:
            output_state = PatchedControlOutputState(_output_state)

        controlled_load_power = d.pop("controlled_load_power", UNSET)

        _override = d.pop("override", UNSET)
        override: Union[Unset, OverrideStatus]
        if isinstance(_override, Unset):
            override = UNSET
        else:
            override = OverrideStatus.from_dict(_override)

        patched_control = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
            name=name,
            state=state,
            commission_date=commission_date,
            active=active,
            last_update=last_update,
            output_state=output_state,
            controlled_load_power=controlled_load_power,
            override=override,
        )

        patched_control.additional_properties = d
        return patched_control

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
