from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="MPPT")


@attr.s(auto_attribs=True)
class MPPT:
    """
    Attributes:
        mppt (int): MPPT number.
        voltage (float): Voltage of the phase.
        current (float): Current of the phase.
    """

    mppt: int
    voltage: float
    current: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mppt = self.mppt
        voltage = self.voltage
        current = self.current

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mppt": mppt,
                "voltage": voltage,
                "current": current,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mppt = d.pop("mppt")

        voltage = d.pop("voltage")

        current = d.pop("current")

        mppt = cls(
            mppt=mppt,
            voltage=voltage,
            current=current,
        )

        mppt.additional_properties = d
        return mppt

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
