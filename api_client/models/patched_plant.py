import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.consumption import Consumption
from ..models.grid_interface import GridInterface
from ..models.patched_plant_state import PatchedPlantState
from ..models.patched_plant_timezone_name import PatchedPlantTimezoneName
from ..models.production import Production
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPlant")


@attr.s(auto_attribs=True)
class PatchedPlant:
    """
    Attributes:
        uuid (Union[Unset, str]): Unique ID of the plant.
        state (Union[Unset, PatchedPlantState]): State of the plant. Possible choices are:<br> 0: Error<br> 1:
            Warning<br> 2: OK<br>
        name (Union[Unset, str]): Name of the plant.
        latitude (Union[Unset, float]): Latitude of the plant coordinates.
        longitude (Union[Unset, float]): Longitude of the plant coordinates.
        timezone_name (Union[Unset, PatchedPlantTimezoneName]): Name of the timezone used for presenting plant
            information.
        commission_date (Union[Unset, datetime.datetime]): Datetime when the plant was first commissioned.
        commissioning_expires (Union[Unset, datetime.datetime]): Datetime when the plant commissioning expires, limiting
            access to some tools.
        reference (Union[Unset, bool]): Can the plant be used as a public reference?
        client (Union[Unset, None, str]): Unique ID of the client account the plant is linked to.
        installer (Union[Unset, None, str]): Unique ID of the installer account the plant is linked to.
        production (Union[Unset, None, Production]):
        consumption (Union[Unset, None, Consumption]):
        grid_interface (Union[Unset, None, GridInterface]):
    """

    uuid: Union[Unset, str] = UNSET
    state: Union[Unset, PatchedPlantState] = UNSET
    name: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    timezone_name: Union[Unset, PatchedPlantTimezoneName] = UNSET
    commission_date: Union[Unset, datetime.datetime] = UNSET
    commissioning_expires: Union[Unset, datetime.datetime] = UNSET
    reference: Union[Unset, bool] = UNSET
    client: Union[Unset, None, str] = UNSET
    installer: Union[Unset, None, str] = UNSET
    production: Union[Unset, None, Production] = UNSET
    consumption: Union[Unset, None, Consumption] = UNSET
    grid_interface: Union[Unset, None, GridInterface] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        name = self.name
        latitude = self.latitude
        longitude = self.longitude
        timezone_name: Union[Unset, str] = UNSET
        if not isinstance(self.timezone_name, Unset):
            timezone_name = self.timezone_name.value

        commission_date: Union[Unset, str] = UNSET
        if not isinstance(self.commission_date, Unset):
            commission_date = self.commission_date.isoformat()

        commissioning_expires: Union[Unset, str] = UNSET
        if not isinstance(self.commissioning_expires, Unset):
            commissioning_expires = self.commissioning_expires.isoformat()

        reference = self.reference
        client = self.client
        installer = self.installer
        production: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.production, Unset):
            production = self.production.to_dict() if self.production else None

        consumption: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.consumption, Unset):
            consumption = self.consumption.to_dict() if self.consumption else None

        grid_interface: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.grid_interface, Unset):
            grid_interface = self.grid_interface.to_dict() if self.grid_interface else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if state is not UNSET:
            field_dict["state"] = state
        if name is not UNSET:
            field_dict["name"] = name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if timezone_name is not UNSET:
            field_dict["timezone_name"] = timezone_name
        if commission_date is not UNSET:
            field_dict["commission_date"] = commission_date
        if commissioning_expires is not UNSET:
            field_dict["commissioning_expires"] = commissioning_expires
        if reference is not UNSET:
            field_dict["reference"] = reference
        if client is not UNSET:
            field_dict["client"] = client
        if installer is not UNSET:
            field_dict["installer"] = installer
        if production is not UNSET:
            field_dict["production"] = production
        if consumption is not UNSET:
            field_dict["consumption"] = consumption
        if grid_interface is not UNSET:
            field_dict["grid_interface"] = grid_interface

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PatchedPlantState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PatchedPlantState(_state)

        name = d.pop("name", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        _timezone_name = d.pop("timezone_name", UNSET)
        timezone_name: Union[Unset, PatchedPlantTimezoneName]
        if isinstance(_timezone_name, Unset):
            timezone_name = UNSET
        else:
            timezone_name = PatchedPlantTimezoneName(_timezone_name)

        _commission_date = d.pop("commission_date", UNSET)
        commission_date: Union[Unset, datetime.datetime]
        if isinstance(_commission_date, Unset):
            commission_date = UNSET
        else:
            commission_date = isoparse(_commission_date)

        _commissioning_expires = d.pop("commissioning_expires", UNSET)
        commissioning_expires: Union[Unset, datetime.datetime]
        if isinstance(_commissioning_expires, Unset):
            commissioning_expires = UNSET
        else:
            commissioning_expires = isoparse(_commissioning_expires)

        reference = d.pop("reference", UNSET)

        client = d.pop("client", UNSET)

        installer = d.pop("installer", UNSET)

        _production = d.pop("production", UNSET)
        production: Union[Unset, None, Production]
        if _production is None:
            production = None
        elif isinstance(_production, Unset):
            production = UNSET
        else:
            production = Production.from_dict(_production)

        _consumption = d.pop("consumption", UNSET)
        consumption: Union[Unset, None, Consumption]
        if _consumption is None:
            consumption = None
        elif isinstance(_consumption, Unset):
            consumption = UNSET
        else:
            consumption = Consumption.from_dict(_consumption)

        _grid_interface = d.pop("grid_interface", UNSET)
        grid_interface: Union[Unset, None, GridInterface]
        if _grid_interface is None:
            grid_interface = None
        elif isinstance(_grid_interface, Unset):
            grid_interface = UNSET
        else:
            grid_interface = GridInterface.from_dict(_grid_interface)

        patched_plant = cls(
            uuid=uuid,
            state=state,
            name=name,
            latitude=latitude,
            longitude=longitude,
            timezone_name=timezone_name,
            commission_date=commission_date,
            commissioning_expires=commissioning_expires,
            reference=reference,
            client=client,
            installer=installer,
            production=production,
            consumption=consumption,
            grid_interface=grid_interface,
        )

        patched_plant.additional_properties = d
        return patched_plant

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
