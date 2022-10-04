from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.panel_installation_installation_type import PanelInstallationInstallationType

T = TypeVar("T", bound="PanelInstallation")


@attr.s(auto_attribs=True)
class PanelInstallation:
    """
    Attributes:
        id (int): ID of the panel installation.
        number_of_panels (int): Number of panels in the installation.
        single_panel_power (int): Nominal power (Wp) of single panel in the installation.
        installation_type (PanelInstallationInstallationType): Type of installation. Possible choices are:<br> 0: Flat
            roof<br> 1: Pitched roof<br> 2: Wall<br> 3: Carport<br> 4: Ground-mounted<br> 99: Other<br>
        tilt (float): Tilt of the panel installation.
        azimuth (float): Azimuth of the panels, south is 0. +90 is west and -90 is east.
    """

    id: int
    number_of_panels: int
    single_panel_power: int
    installation_type: PanelInstallationInstallationType
    tilt: float
    azimuth: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        number_of_panels = self.number_of_panels
        single_panel_power = self.single_panel_power
        installation_type = self.installation_type.value

        tilt = self.tilt
        azimuth = self.azimuth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number_of_panels": number_of_panels,
                "single_panel_power": single_panel_power,
                "installation_type": installation_type,
                "tilt": tilt,
                "azimuth": azimuth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        number_of_panels = d.pop("number_of_panels")

        single_panel_power = d.pop("single_panel_power")

        installation_type = PanelInstallationInstallationType(d.pop("installation_type"))

        tilt = d.pop("tilt")

        azimuth = d.pop("azimuth")

        panel_installation = cls(
            id=id,
            number_of_panels=number_of_panels,
            single_panel_power=single_panel_power,
            installation_type=installation_type,
            tilt=tilt,
            azimuth=azimuth,
        )

        panel_installation.additional_properties = d
        return panel_installation

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
