from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.production_energy import ProductionEnergy

T = TypeVar("T", bound="Production")


@attr.s(auto_attribs=True)
class Production:
    """
    Attributes:
        power (Optional[int]): Produced power in watts (W).
        energy (Optional[ProductionEnergy]):
        panel_power (Optional[int]): Nominal power of solar panels in wattpeaks (Wp).
    """

    power: Optional[int]
    energy: Optional[ProductionEnergy]
    panel_power: Optional[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        power = self.power
        energy = self.energy.to_dict() if self.energy else None

        panel_power = self.panel_power

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "power": power,
                "energy": energy,
                "panel_power": panel_power,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        power = d.pop("power")

        _energy = d.pop("energy")
        energy: Optional[ProductionEnergy]
        if _energy is None:
            energy = None
        else:
            energy = ProductionEnergy.from_dict(_energy)

        panel_power = d.pop("panel_power")

        production = cls(
            power=power,
            energy=energy,
            panel_power=panel_power,
        )

        production.additional_properties = d
        return production

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
