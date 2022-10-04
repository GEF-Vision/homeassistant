import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.heatpump_device_state import HeatpumpDeviceState
from ..models.heatpump_device_type import HeatpumpDeviceType
from ..models.heatpump_operating_mode import HeatpumpOperatingMode
from ..models.heatpump_state import HeatpumpState
from ..models.override_heatpump import OverrideHeatpump
from ..types import UNSET, Unset

T = TypeVar("T", bound="Heatpump")


@attr.s(auto_attribs=True)
class Heatpump:
    """
    Attributes:
        gateway (DeviceGateway):
        device_type (HeatpumpDeviceType): Device type
        id (int): Unique (per device-type) identifier of the device.
        state (HeatpumpState): State of the device. Possible choices are:<br> 0: Error<br> 1: Warning<br> 2: OK<br>
        commission_date (datetime.date): Date when the device was commissioned.
        active (bool): Is the device active? Devices can become inactive for example when exchanged to a new one.
        last_update (datetime.datetime): Time of last update for device measurements.
        device_state (HeatpumpDeviceState): State of the heat pump. Possible choices are:<br> 0: Unknown<br> 1: Off<br>
            2: On<br>
        mode (HeatpumpOperatingMode): Operating mode of the heat pump. Possible choices are:<br> 0: auto<br> 1: heat<br>
            2: dry<br> 3: fan<br> 4: cool<br>
        temperature_setpoint (float): Temperature setpoint, used for controlling the pump.
        temperature_reference (float): Temperature reference, measured by the pump.
        operating_time (int): Heatpump operating time in hours.
        alarm (bool): Is there an active alarm.
        error_code (int): Heatpump error code (if exists).
        override (OverrideHeatpump):
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
    """

    gateway: DeviceGateway
    device_type: HeatpumpDeviceType
    id: int
    state: HeatpumpState
    commission_date: datetime.date
    active: bool
    last_update: datetime.datetime
    device_state: HeatpumpDeviceState
    mode: HeatpumpOperatingMode
    temperature_setpoint: float
    temperature_reference: float
    operating_time: int
    alarm: bool
    error_code: int
    override: OverrideHeatpump
    name: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateway = self.gateway.to_dict()

        device_type = self.device_type.value

        id = self.id
        state = self.state.value

        commission_date = self.commission_date.isoformat()
        active = self.active
        last_update = self.last_update.isoformat()

        device_state = self.device_state.value

        mode = self.mode.value

        temperature_setpoint = self.temperature_setpoint
        temperature_reference = self.temperature_reference
        operating_time = self.operating_time
        alarm = self.alarm
        error_code = self.error_code
        override = self.override.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateway": gateway,
                "device_type": device_type,
                "id": id,
                "state": state,
                "commission_date": commission_date,
                "active": active,
                "last_update": last_update,
                "device_state": device_state,
                "mode": mode,
                "temperature_setpoint": temperature_setpoint,
                "temperature_reference": temperature_reference,
                "operating_time": operating_time,
                "alarm": alarm,
                "error_code": error_code,
                "override": override,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gateway = DeviceGateway.from_dict(d.pop("gateway"))

        device_type = HeatpumpDeviceType(d.pop("device_type"))

        id = d.pop("id")

        state = HeatpumpState(d.pop("state"))

        commission_date = isoparse(d.pop("commission_date")).date()

        active = d.pop("active")

        last_update = isoparse(d.pop("last_update"))

        device_state = HeatpumpDeviceState(d.pop("device_state"))

        mode = HeatpumpOperatingMode(d.pop("mode"))

        temperature_setpoint = d.pop("temperature_setpoint")

        temperature_reference = d.pop("temperature_reference")

        operating_time = d.pop("operating_time")

        alarm = d.pop("alarm")

        error_code = d.pop("error_code")

        override = OverrideHeatpump.from_dict(d.pop("override"))

        name = d.pop("name", UNSET)

        heatpump = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
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
            name=name,
        )

        heatpump.additional_properties = d
        return heatpump

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
