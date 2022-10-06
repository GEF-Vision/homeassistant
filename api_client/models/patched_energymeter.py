import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.energymeter_energy import EnergymeterEnergy
from ..models.energymeter_phase import EnergymeterPhase
from ..models.energymeter_power import EnergymeterPower
from ..models.patched_energymeter_device_type import PatchedEnergymeterDeviceType
from ..models.patched_energymeter_meter_type import PatchedEnergymeterMeterType
from ..models.patched_energymeter_state import PatchedEnergymeterState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEnergymeter")


@attr.s(auto_attribs=True)
class PatchedEnergymeter:
    """
    Attributes:
        gateway (Union[Unset, DeviceGateway]):
        device_type (Union[Unset, PatchedEnergymeterDeviceType]): Device type
        id (Union[Unset, int]): Unique (per device-type) identifier of the device.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
        state (Union[Unset, PatchedEnergymeterState]): State of the device. Possible choices are:<br> 0: Error<br> 1:
            Warning<br> 2: OK<br>
        commission_date (Union[Unset, datetime.date]): Date when the device was commissioned.
        active (Union[Unset, bool]): Is the device active? Devices can become inactive for example when exchanged to a
            new one.
        last_update (Union[Unset, datetime.datetime]): Time of last update for device measurements.
        meter_type (Union[Unset, PatchedEnergymeterMeterType]): Type of the energymeter. Possible values are: <br> 0:
            Grid interface<br> 1: Consumption<br> 2: Production<br>
        power (Union[Unset, EnergymeterPower]):
        energy (Union[Unset, EnergymeterEnergy]):
        phase (Union[Unset, List[EnergymeterPhase]]): Measurements for AC phases.
    """

    gateway: Union[Unset, DeviceGateway] = UNSET
    device_type: Union[Unset, PatchedEnergymeterDeviceType] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = ""
    state: Union[Unset, PatchedEnergymeterState] = UNSET
    commission_date: Union[Unset, datetime.date] = UNSET
    active: Union[Unset, bool] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    meter_type: Union[Unset, PatchedEnergymeterMeterType] = UNSET
    power: Union[Unset, EnergymeterPower] = UNSET
    energy: Union[Unset, EnergymeterEnergy] = UNSET
    phase: Union[Unset, List[EnergymeterPhase]] = UNSET
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

        meter_type: Union[Unset, int] = UNSET
        if not isinstance(self.meter_type, Unset):
            meter_type = self.meter_type.value

        power: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.power, Unset):
            power = self.power.to_dict()

        energy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.energy, Unset):
            energy = self.energy.to_dict()

        phase: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phase, Unset):
            phase = []
            for phase_item_data in self.phase:
                phase_item = phase_item_data.to_dict()

                phase.append(phase_item)

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
        if meter_type is not UNSET:
            field_dict["meter_type"] = meter_type
        if power is not UNSET:
            field_dict["power"] = power
        if energy is not UNSET:
            field_dict["energy"] = energy
        if phase is not UNSET:
            field_dict["phase"] = phase

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
        device_type: Union[Unset, PatchedEnergymeterDeviceType]
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = PatchedEnergymeterDeviceType(_device_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PatchedEnergymeterState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PatchedEnergymeterState(_state)

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

        _meter_type = d.pop("meter_type", UNSET)
        meter_type: Union[Unset, PatchedEnergymeterMeterType]
        if isinstance(_meter_type, Unset):
            meter_type = UNSET
        else:
            meter_type = PatchedEnergymeterMeterType(_meter_type)

        _power = d.pop("power", UNSET)
        power: Union[Unset, EnergymeterPower]
        if isinstance(_power, Unset):
            power = UNSET
        else:
            power = EnergymeterPower.from_dict(_power)

        _energy = d.pop("energy", UNSET)
        energy: Union[Unset, EnergymeterEnergy]
        if isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = EnergymeterEnergy.from_dict(_energy)

        phase = []
        _phase = d.pop("phase", UNSET)
        for phase_item_data in _phase or []:
            phase_item = EnergymeterPhase.from_dict(phase_item_data)

            phase.append(phase_item)

        patched_energymeter = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
            name=name,
            state=state,
            commission_date=commission_date,
            active=active,
            last_update=last_update,
            meter_type=meter_type,
            power=power,
            energy=energy,
            phase=phase,
        )

        patched_energymeter.additional_properties = d
        return patched_energymeter

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
