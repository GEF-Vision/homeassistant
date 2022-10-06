from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.patched_panel_installation_installation_type import PatchedPanelInstallationInstallationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPanelInstallation")


@attr.s(auto_attribs=True)
class PatchedPanelInstallation:
    """
    Attributes:
        id (Union[Unset, int]): ID of the panel installation.
        number_of_panels (Union[Unset, int]): Number of panels in the installation.
        single_panel_power (Union[Unset, int]): Nominal power (Wp) of single panel in the installation.
        installation_type (Union[Unset, PatchedPanelInstallationInstallationType]): Type of installation. Possible
            choices are:<br> 0: Flat roof<br> 1: Pitched roof<br> 2: Wall<br> 3: Carport<br> 4: Ground-mounted<br> 99:
            Other<br>
        tilt (Union[Unset, float]): Tilt of the panel installation.
        azimuth (Union[Unset, float]): Azimuth of the panels, south is 0. +90 is west and -90 is east.
    """

    id: Union[Unset, int] = UNSET
    number_of_panels: Union[Unset, int] = UNSET
    single_panel_power: Union[Unset, int] = UNSET
    installation_type: Union[Unset, PatchedPanelInstallationInstallationType] = UNSET
    tilt: Union[Unset, float] = UNSET
    azimuth: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        number_of_panels = self.number_of_panels
        single_panel_power = self.single_panel_power
        installation_type: Union[Unset, int] = UNSET
        if not isinstance(self.installation_type, Unset):
            installation_type = self.installation_type.value

        tilt = self.tilt
        azimuth = self.azimuth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if number_of_panels is not UNSET:
            field_dict["number_of_panels"] = number_of_panels
        if single_panel_power is not UNSET:
            field_dict["single_panel_power"] = single_panel_power
        if installation_type is not UNSET:
            field_dict["installation_type"] = installation_type
        if tilt is not UNSET:
            field_dict["tilt"] = tilt
        if azimuth is not UNSET:
            field_dict["azimuth"] = azimuth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        number_of_panels = d.pop("number_of_panels", UNSET)

        single_panel_power = d.pop("single_panel_power", UNSET)

        _installation_type = d.pop("installation_type", UNSET)
        installation_type: Union[Unset, PatchedPanelInstallationInstallationType]
        if isinstance(_installation_type, Unset):
            installation_type = UNSET
        else:
            installation_type = PatchedPanelInstallationInstallationType(_installation_type)

        tilt = d.pop("tilt", UNSET)

        azimuth = d.pop("azimuth", UNSET)

        patched_panel_installation = cls(
            id=id,
            number_of_panels=number_of_panels,
            single_panel_power=single_panel_power,
            installation_type=installation_type,
            tilt=tilt,
            azimuth=azimuth,
        )

        patched_panel_installation.additional_properties = d
        return patched_panel_installation

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
