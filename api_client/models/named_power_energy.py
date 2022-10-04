from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.energy_counter import EnergyCounter
from ..types import UNSET, Unset

T = TypeVar("T", bound="NamedPowerEnergy")


@attr.s(auto_attribs=True)
class NamedPowerEnergy:
    """
    Attributes:
        pk (Union[Unset, None, int]): Primary key of the device, if data links directly to a device.
        name (Union[Unset, str]):  Default: ''.
        power (Union[Unset, None, int]): Transferred power in watts (W).
        energy (Union[Unset, None, EnergyCounter]):
    """

    pk: Union[Unset, None, int] = UNSET
    name: Union[Unset, str] = ""
    power: Union[Unset, None, int] = UNSET
    energy: Union[Unset, None, EnergyCounter] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pk = self.pk
        name = self.name
        power = self.power
        energy: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.energy, Unset):
            energy = self.energy.to_dict() if self.energy else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pk is not UNSET:
            field_dict["pk"] = pk
        if name is not UNSET:
            field_dict["name"] = name
        if power is not UNSET:
            field_dict["power"] = power
        if energy is not UNSET:
            field_dict["energy"] = energy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pk = d.pop("pk", UNSET)

        name = d.pop("name", UNSET)

        power = d.pop("power", UNSET)

        _energy = d.pop("energy", UNSET)
        energy: Union[Unset, None, EnergyCounter]
        if _energy is None:
            energy = None
        elif isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = EnergyCounter.from_dict(_energy)

        named_power_energy = cls(
            pk=pk,
            name=name,
            power=power,
            energy=energy,
        )

        named_power_energy.additional_properties = d
        return named_power_energy

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
