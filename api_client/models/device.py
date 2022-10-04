import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_device_type import DeviceDeviceType
from ..models.device_gateway import DeviceGateway
from ..models.device_state import DeviceState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Device")


@attr.s(auto_attribs=True)
class Device:
    """
    Attributes:
        gateway (DeviceGateway):
        device_type (DeviceDeviceType): Device type
        id (int): Unique (per device-type) identifier of the device.
        state (DeviceState): State of the device. Possible choices are:<br> 0: Error<br> 1: Warning<br> 2: OK<br>
        commission_date (datetime.date): Date when the device was commissioned.
        active (bool): Is the device active? Devices can become inactive for example when exchanged to a new one.
        last_update (datetime.datetime): Time of last update for device measurements.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
    """

    gateway: DeviceGateway
    device_type: DeviceDeviceType
    id: int
    state: DeviceState
    commission_date: datetime.date
    active: bool
    last_update: datetime.datetime
    name: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateway = self.gateway.to_dict()

        device_type = self.device_type.value

        id = self.id
        state = self.state.value

        commission_date = self.commission_date.isoformat()
        active = self.active
        last_update = self.last_update.isoformat()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateway": gateway,
                "device_type": device_type,
                "id": id,
                "state": state,
                "commission_date": commission_date,
                "active": active,
                "last_update": last_update,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gateway = DeviceGateway.from_dict(d.pop("gateway"))

        device_type = DeviceDeviceType(d.pop("device_type"))

        id = d.pop("id")

        state = DeviceState(d.pop("state"))

        commission_date = isoparse(d.pop("commission_date")).date()

        active = d.pop("active")

        last_update = isoparse(d.pop("last_update"))

        name = d.pop("name", UNSET)

        device = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
            state=state,
            commission_date=commission_date,
            active=active,
            last_update=last_update,
            name=name,
        )

        device.additional_properties = d
        return device

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
