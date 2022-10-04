import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.consumption import Consumption
from ..models.grid_interface import GridInterface
from ..models.plant_state import PlantState
from ..models.plant_timezone_name import PlantTimezoneName
from ..models.production import Production

T = TypeVar("T", bound="Plant")


@attr.s(auto_attribs=True)
class Plant:
    """
    Attributes:
        uuid (str): Unique ID of the plant.
        state (PlantState): State of the plant. Possible choices are:<br> 0: Error<br> 1: Warning<br> 2: OK<br>
        name (str): Name of the plant.
        latitude (float): Latitude of the plant coordinates.
        longitude (float): Longitude of the plant coordinates.
        timezone_name (PlantTimezoneName): Name of the timezone used for presenting plant information.
        commission_date (datetime.datetime): Datetime when the plant was first commissioned.
        commissioning_expires (datetime.datetime): Datetime when the plant commissioning expires, limiting access to
            some tools.
        reference (bool): Can the plant be used as a public reference?
        client (Optional[str]): Unique ID of the client account the plant is linked to.
        installer (Optional[str]): Unique ID of the installer account the plant is linked to.
        production (Optional[Production]):
        consumption (Optional[Consumption]):
        grid_interface (Optional[GridInterface]):
    """

    uuid: str
    state: PlantState
    name: str
    latitude: float
    longitude: float
    timezone_name: PlantTimezoneName
    commission_date: datetime.datetime
    commissioning_expires: datetime.datetime
    reference: bool
    client: Optional[str]
    installer: Optional[str]
    production: Optional[Production]
    consumption: Optional[Consumption]
    grid_interface: Optional[GridInterface]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        state = self.state.value

        name = self.name
        latitude = self.latitude
        longitude = self.longitude
        timezone_name = self.timezone_name.value

        commission_date = self.commission_date.isoformat()

        commissioning_expires = self.commissioning_expires.isoformat()

        reference = self.reference
        client = self.client
        installer = self.installer
        production = self.production.to_dict() if self.production else None

        consumption = self.consumption.to_dict() if self.consumption else None

        grid_interface = self.grid_interface.to_dict() if self.grid_interface else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "state": state,
                "name": name,
                "latitude": latitude,
                "longitude": longitude,
                "timezone_name": timezone_name,
                "commission_date": commission_date,
                "commissioning_expires": commissioning_expires,
                "reference": reference,
                "client": client,
                "installer": installer,
                "production": production,
                "consumption": consumption,
                "grid_interface": grid_interface,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        state = PlantState(d.pop("state"))

        name = d.pop("name")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        timezone_name = PlantTimezoneName(d.pop("timezone_name"))

        commission_date = isoparse(d.pop("commission_date"))

        commissioning_expires = isoparse(d.pop("commissioning_expires"))

        reference = d.pop("reference")

        client = d.pop("client")

        installer = d.pop("installer")

        _production = d.pop("production")
        production: Optional[Production]
        if _production is None:
            production = None
        else:
            production = Production.from_dict(_production)

        _consumption = d.pop("consumption")
        consumption: Optional[Consumption]
        if _consumption is None:
            consumption = None
        else:
            consumption = Consumption.from_dict(_consumption)

        _grid_interface = d.pop("grid_interface")
        grid_interface: Optional[GridInterface]
        if _grid_interface is None:
            grid_interface = None
        else:
            grid_interface = GridInterface.from_dict(_grid_interface)

        plant = cls(
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

        plant.additional_properties = d
        return plant

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
