import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.patched_sensor_device_type import PatchedSensorDeviceType
from ..models.patched_sensor_sensor_type import PatchedSensorSensorType
from ..models.patched_sensor_state import PatchedSensorState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSensor")


@attr.s(auto_attribs=True)
class PatchedSensor:
    """
    Attributes:
        gateway (Union[Unset, DeviceGateway]):
        device_type (Union[Unset, PatchedSensorDeviceType]): Device type
        id (Union[Unset, int]): Unique (per device-type) identifier of the device.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
        state (Union[Unset, PatchedSensorState]): State of the device. Possible choices are:<br> 0: Error<br> 1:
            Warning<br> 2: OK<br>
        commission_date (Union[Unset, datetime.date]): Date when the device was commissioned.
        active (Union[Unset, bool]): Is the device active? Devices can become inactive for example when exchanged to a
            new one.
        last_update (Union[Unset, datetime.datetime]): Time of last update for device measurements.
        sensor_type (Union[Unset, PatchedSensorSensorType]): Type of the sensor.
        value (Union[Unset, None, float]): Current value of the sensor.
    """

    gateway: Union[Unset, DeviceGateway] = UNSET
    device_type: Union[Unset, PatchedSensorDeviceType] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = ""
    state: Union[Unset, PatchedSensorState] = UNSET
    commission_date: Union[Unset, datetime.date] = UNSET
    active: Union[Unset, bool] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    sensor_type: Union[Unset, PatchedSensorSensorType] = UNSET
    value: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gateway: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.to_dict()

        device_type: Union[Unset, str] = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type.value

        id = self.id
        name = self.name
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        commission_date: Union[Unset, str] = UNSET
        if not isinstance(self.commission_date, Unset):
            commission_date = self.commission_date.isoformat()

        active = self.active
        last_update: Union[Unset, str] = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

        sensor_type: Union[Unset, str] = UNSET
        if not isinstance(self.sensor_type, Unset):
            sensor_type = self.sensor_type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if commission_date is not UNSET:
            field_dict["commission_date"] = commission_date
        if active is not UNSET:
            field_dict["active"] = active
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if sensor_type is not UNSET:
            field_dict["sensor_type"] = sensor_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _gateway = d.pop("gateway", UNSET)
        gateway: Union[Unset, DeviceGateway]
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = DeviceGateway.from_dict(_gateway)

        _device_type = d.pop("device_type", UNSET)
        device_type: Union[Unset, PatchedSensorDeviceType]
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = PatchedSensorDeviceType(_device_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PatchedSensorState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PatchedSensorState(_state)

        _commission_date = d.pop("commission_date", UNSET)
        commission_date: Union[Unset, datetime.date]
        if isinstance(_commission_date, Unset):
            commission_date = UNSET
        else:
            commission_date = isoparse(_commission_date).date()

        active = d.pop("active", UNSET)

        _last_update = d.pop("last_update", UNSET)
        last_update: Union[Unset, datetime.datetime]
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update)

        _sensor_type = d.pop("sensor_type", UNSET)
        sensor_type: Union[Unset, PatchedSensorSensorType]
        if isinstance(_sensor_type, Unset):
            sensor_type = UNSET
        else:
            sensor_type = PatchedSensorSensorType(_sensor_type)

        value = d.pop("value", UNSET)

        patched_sensor = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
            name=name,
            state=state,
            commission_date=commission_date,
            active=active,
            last_update=last_update,
            sensor_type=sensor_type,
            value=value,
        )

        patched_sensor.additional_properties = d
        return patched_sensor

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
