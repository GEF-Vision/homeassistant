import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.override_heatpump import OverrideHeatpump
from ..models.patched_heatpump_device_state import PatchedHeatpumpDeviceState
from ..models.patched_heatpump_device_type import PatchedHeatpumpDeviceType
from ..models.patched_heatpump_operating_mode import PatchedHeatpumpOperatingMode
from ..models.patched_heatpump_state import PatchedHeatpumpState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedHeatpump")


@attr.s(auto_attribs=True)
class PatchedHeatpump:
    """
    Attributes:
        gateway (Union[Unset, DeviceGateway]):
        device_type (Union[Unset, PatchedHeatpumpDeviceType]): Device type
        id (Union[Unset, int]): Unique (per device-type) identifier of the device.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
        state (Union[Unset, PatchedHeatpumpState]): State of the device. Possible choices are:<br> 0: Error<br> 1:
            Warning<br> 2: OK<br>
        commission_date (Union[Unset, datetime.date]): Date when the device was commissioned.
        active (Union[Unset, bool]): Is the device active? Devices can become inactive for example when exchanged to a
            new one.
        last_update (Union[Unset, datetime.datetime]): Time of last update for device measurements.
        device_state (Union[Unset, PatchedHeatpumpDeviceState]): State of the heat pump. Possible choices are:<br> 0:
            Unknown<br> 1: Off<br> 2: On<br>
        mode (Union[Unset, PatchedHeatpumpOperatingMode]): Operating mode of the heat pump. Possible choices are:<br> 0:
            auto<br> 1: heat<br> 2: dry<br> 3: fan<br> 4: cool<br>
        temperature_setpoint (Union[Unset, float]): Temperature setpoint, used for controlling the pump.
        temperature_reference (Union[Unset, float]): Temperature reference, measured by the pump.
        operating_time (Union[Unset, int]): Heatpump operating time in hours.
        alarm (Union[Unset, bool]): Is there an active alarm.
        error_code (Union[Unset, int]): Heatpump error code (if exists).
        override (Union[Unset, OverrideHeatpump]):
    """

    gateway: Union[Unset, DeviceGateway] = UNSET
    device_type: Union[Unset, PatchedHeatpumpDeviceType] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = ""
    state: Union[Unset, PatchedHeatpumpState] = UNSET
    commission_date: Union[Unset, datetime.date] = UNSET
    active: Union[Unset, bool] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    device_state: Union[Unset, PatchedHeatpumpDeviceState] = UNSET
    mode: Union[Unset, PatchedHeatpumpOperatingMode] = UNSET
    temperature_setpoint: Union[Unset, float] = UNSET
    temperature_reference: Union[Unset, float] = UNSET
    operating_time: Union[Unset, int] = UNSET
    alarm: Union[Unset, bool] = UNSET
    error_code: Union[Unset, int] = UNSET
    override: Union[Unset, OverrideHeatpump] = UNSET
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

        device_state: Union[Unset, int] = UNSET
        if not isinstance(self.device_state, Unset):
            device_state = self.device_state.value

        mode: Union[Unset, int] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        temperature_setpoint = self.temperature_setpoint
        temperature_reference = self.temperature_reference
        operating_time = self.operating_time
        alarm = self.alarm
        error_code = self.error_code
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
        if device_state is not UNSET:
            field_dict["device_state"] = device_state
        if mode is not UNSET:
            field_dict["mode"] = mode
        if temperature_setpoint is not UNSET:
            field_dict["temperature_setpoint"] = temperature_setpoint
        if temperature_reference is not UNSET:
            field_dict["temperature_reference"] = temperature_reference
        if operating_time is not UNSET:
            field_dict["operating_time"] = operating_time
        if alarm is not UNSET:
            field_dict["alarm"] = alarm
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
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
        device_type: Union[Unset, PatchedHeatpumpDeviceType]
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = PatchedHeatpumpDeviceType(_device_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PatchedHeatpumpState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PatchedHeatpumpState(_state)

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

        _device_state = d.pop("device_state", UNSET)
        device_state: Union[Unset, PatchedHeatpumpDeviceState]
        if isinstance(_device_state, Unset):
            device_state = UNSET
        else:
            device_state = PatchedHeatpumpDeviceState(_device_state)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, PatchedHeatpumpOperatingMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = PatchedHeatpumpOperatingMode(_mode)

        temperature_setpoint = d.pop("temperature_setpoint", UNSET)

        temperature_reference = d.pop("temperature_reference", UNSET)

        operating_time = d.pop("operating_time", UNSET)

        alarm = d.pop("alarm", UNSET)

        error_code = d.pop("error_code", UNSET)

        _override = d.pop("override", UNSET)
        override: Union[Unset, OverrideHeatpump]
        if isinstance(_override, Unset):
            override = UNSET
        else:
            override = OverrideHeatpump.from_dict(_override)

        patched_heatpump = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
            name=name,
            state=state,
            commission_date=commission_date,
            active=active,
            last_update=last_update,
            device_state=device_state,
            mode=mode,
            temperature_setpoint=temperature_setpoint,
            temperature_reference=temperature_reference,
            operating_time=operating_time,
            alarm=alarm,
            error_code=error_code,
            override=override,
        )

        patched_heatpump.additional_properties = d
        return patched_heatpump

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
