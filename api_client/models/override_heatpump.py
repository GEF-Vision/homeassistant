import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.override_heatpump_device_state import OverrideHeatpumpDeviceState
from ..models.override_heatpump_operating_mode import OverrideHeatpumpOperatingMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="OverrideHeatpump")


@attr.s(auto_attribs=True)
class OverrideHeatpump:
    """
    Attributes:
        device_state (OverrideHeatpumpDeviceState): State of the heat pump. Possible choices are:<br> 1: Off<br> 2:
            On<br>
        mode (OverrideHeatpumpOperatingMode): Operating mode of the heat pump. Possible choices are:<br> 0: auto<br> 1:
            heat<br> 2: dry<br> 3: fan<br> 4: cool<br>
        temperature_setpoint (float): Temperature setpoint, used for controlling the pump.
        start (Union[Unset, datetime.datetime]): Start time of the override period. Defaults to current datetime.
        end (Union[Unset, datetime.datetime]): End time of the override period. Defaults to current datetime + 1 hour.
    """

    device_state: OverrideHeatpumpDeviceState
    mode: OverrideHeatpumpOperatingMode
    temperature_setpoint: float
    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_state = self.device_state.value

        mode = self.mode.value

        temperature_setpoint = self.temperature_setpoint
        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_state": device_state,
                "mode": mode,
                "temperature_setpoint": temperature_setpoint,
            }
        )
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_state = OverrideHeatpumpDeviceState(d.pop("device_state"))

        mode = OverrideHeatpumpOperatingMode(d.pop("mode"))

        temperature_setpoint = d.pop("temperature_setpoint")

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

        override_heatpump = cls(
            device_state=device_state,
            mode=mode,
            temperature_setpoint=temperature_setpoint,
            start=start,
            end=end,
        )

        override_heatpump.additional_properties = d
        return override_heatpump

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
