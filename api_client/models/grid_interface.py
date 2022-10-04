from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.energymeter_energy import EnergymeterEnergy
from ..models.energymeter_power import EnergymeterPower

T = TypeVar("T", bound="GridInterface")


@attr.s(auto_attribs=True)
class GridInterface:
    """
    Attributes:
        power (Optional[EnergymeterPower]):
        energy (Optional[EnergymeterEnergy]):
    """

    power: Optional[EnergymeterPower]
    energy: Optional[EnergymeterEnergy]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        power = self.power.to_dict() if self.power else None

        energy = self.energy.to_dict() if self.energy else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "power": power,
                "energy": energy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _power = d.pop("power")
        power: Optional[EnergymeterPower]
        if _power is None:
            power = None
        else:
            power = EnergymeterPower.from_dict(_power)

        _energy = d.pop("energy")
        energy: Optional[EnergymeterEnergy]
        if _energy is None:
            energy = None
        else:
            energy = EnergymeterEnergy.from_dict(_energy)

        grid_interface = cls(
            power=power,
            energy=energy,
        )

        grid_interface.additional_properties = d
        return grid_interface

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
