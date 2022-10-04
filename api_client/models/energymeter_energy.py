from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.energy_counter import EnergyCounter

T = TypeVar("T", bound="EnergymeterEnergy")


@attr.s(auto_attribs=True)
class EnergymeterEnergy:
    """
    Attributes:
        import_ (Optional[EnergyCounter]):
        export (Optional[EnergyCounter]):
    """

    import_: Optional[EnergyCounter]
    export: Optional[EnergyCounter]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        import_ = self.import_.to_dict() if self.import_ else None

        export = self.export.to_dict() if self.export else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "import": import_,
                "export": export,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _import_ = d.pop("import")
        import_: Optional[EnergyCounter]
        if _import_ is None:
            import_ = None
        else:
            import_ = EnergyCounter.from_dict(_import_)

        _export = d.pop("export")
        export: Optional[EnergyCounter]
        if _export is None:
            export = None
        else:
            export = EnergyCounter.from_dict(_export)

        energymeter_energy = cls(
            import_=import_,
            export=export,
        )

        energymeter_energy.additional_properties = d
        return energymeter_energy

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
