from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.consumption_energy import ConsumptionEnergy
from ..types import UNSET, Unset

T = TypeVar("T", bound="Consumption")


@attr.s(auto_attribs=True)
class Consumption:
    """
    Attributes:
        power (Union[Unset, None, int]): Consumed power in watts (W).
        energy (Union[Unset, None, ConsumptionEnergy]):
    """

    power: Union[Unset, None, int] = UNSET
    energy: Union[Unset, None, ConsumptionEnergy] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        power = self.power
        energy: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.energy, Unset):
            energy = self.energy.to_dict() if self.energy else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if power is not UNSET:
            field_dict["power"] = power
        if energy is not UNSET:
            field_dict["energy"] = energy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        power = d.pop("power", UNSET)

        _energy = d.pop("energy", UNSET)
        energy: Union[Unset, None, ConsumptionEnergy]
        if _energy is None:
            energy = None
        elif isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = ConsumptionEnergy.from_dict(_energy)

        consumption = cls(
            power=power,
            energy=energy,
        )

        consumption.additional_properties = d
        return consumption

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
