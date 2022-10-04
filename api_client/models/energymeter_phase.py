from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EnergymeterPhase")


@attr.s(auto_attribs=True)
class EnergymeterPhase:
    """
    Attributes:
        phase (str): Phase name, possible values are "L1", "L2", and "L3".
        voltage (float): Voltage of the phase.
        current (float): Current of the phase.
        active_power (int): Active power of the phase.
        reactive_power (int): Reactive power of the phase.
    """

    phase: str
    voltage: float
    current: float
    active_power: int
    reactive_power: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phase = self.phase
        voltage = self.voltage
        current = self.current
        active_power = self.active_power
        reactive_power = self.reactive_power

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phase": phase,
                "voltage": voltage,
                "current": current,
                "active_power": active_power,
                "reactive_power": reactive_power,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        phase = d.pop("phase")

        voltage = d.pop("voltage")

        current = d.pop("current")

        active_power = d.pop("active_power")

        reactive_power = d.pop("reactive_power")

        energymeter_phase = cls(
            phase=phase,
            voltage=voltage,
            current=current,
            active_power=active_power,
            reactive_power=reactive_power,
        )

        energymeter_phase.additional_properties = d
        return energymeter_phase

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
