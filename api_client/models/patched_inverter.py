import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.inverter_production import InverterProduction
from ..models.mppt import MPPT
from ..models.patched_inverter_device_type import PatchedInverterDeviceType
from ..models.patched_inverter_extended_state import PatchedInverterExtendedState
from ..models.patched_inverter_state import PatchedInverterState
from ..models.phase import Phase
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedInverter")


@attr.s(auto_attribs=True)
class PatchedInverter:
    """
    Attributes:
        gateway (Union[Unset, DeviceGateway]):
        device_type (Union[Unset, PatchedInverterDeviceType]): Device type
        id (Union[Unset, int]): Unique (per device-type) identifier of the device.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
        state (Union[Unset, PatchedInverterState]): State of the device. Possible choices are:<br> 0: Error<br> 1:
            Warning<br> 2: OK<br>
        commission_date (Union[Unset, datetime.date]): Date when the device was commissioned.
        active (Union[Unset, bool]): Is the device active? Devices can become inactive for example when exchanged to a
            new one.
        last_update (Union[Unset, datetime.datetime]): Time of last update for device measurements.
        extended_state (Union[Unset, PatchedInverterExtendedState]): Extended state of the inverter. Possible choices
            are:<br> 0: Unknown<br> 1: Off<br> 2: Sleep<br> 3: Starting<br> 4: Run<br> 5: Throttle<br> 6: Shutting down<br>
            7: Fault<br> 8: Standby<br> 9: Warning<br> 10: Read error<br> 11: No production in 24 hours<br> 12: No
            communication in 24 hours<br>
        model_name (Union[Unset, str]): Model name of the inverter.
        nominal_power (Union[Unset, int]): Nominal power of the inverter in watts (W).
        power (Union[Unset, int]): Inverter active power in watts (W).
        energy (Union[Unset, InverterProduction]):
        phase (Union[Unset, List[Phase]]): Measurements for AC phases.
        mppt (Union[Unset, List[MPPT]]): Measurements for MPPT trackers.
    """

    gateway: Union[Unset, DeviceGateway] = UNSET
    device_type: Union[Unset, PatchedInverterDeviceType] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = ""
    state: Union[Unset, PatchedInverterState] = UNSET
    commission_date: Union[Unset, datetime.date] = UNSET
    active: Union[Unset, bool] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    extended_state: Union[Unset, PatchedInverterExtendedState] = UNSET
    model_name: Union[Unset, str] = UNSET
    nominal_power: Union[Unset, int] = UNSET
    power: Union[Unset, int] = UNSET
    energy: Union[Unset, InverterProduction] = UNSET
    phase: Union[Unset, List[Phase]] = UNSET
    mppt: Union[Unset, List[MPPT]] = UNSET
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

        extended_state: Union[Unset, int] = UNSET
        if not isinstance(self.extended_state, Unset):
            extended_state = self.extended_state.value

        model_name = self.model_name
        nominal_power = self.nominal_power
        power = self.power
        energy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.energy, Unset):
            energy = self.energy.to_dict()

        phase: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phase, Unset):
            phase = []
            for phase_item_data in self.phase:
                phase_item = phase_item_data.to_dict()

                phase.append(phase_item)

        mppt: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mppt, Unset):
            mppt = []
            for mppt_item_data in self.mppt:
                mppt_item = mppt_item_data.to_dict()

                mppt.append(mppt_item)

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
        if extended_state is not UNSET:
            field_dict["extended_state"] = extended_state
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if nominal_power is not UNSET:
            field_dict["nominal_power"] = nominal_power
        if power is not UNSET:
            field_dict["power"] = power
        if energy is not UNSET:
            field_dict["energy"] = energy
        if phase is not UNSET:
            field_dict["phase"] = phase
        if mppt is not UNSET:
            field_dict["mppt"] = mppt

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
        device_type: Union[Unset, PatchedInverterDeviceType]
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = PatchedInverterDeviceType(_device_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PatchedInverterState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PatchedInverterState(_state)

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

        _extended_state = d.pop("extended_state", UNSET)
        extended_state: Union[Unset, PatchedInverterExtendedState]
        if isinstance(_extended_state, Unset):
            extended_state = UNSET
        else:
            extended_state = PatchedInverterExtendedState(_extended_state)

        model_name = d.pop("model_name", UNSET)

        nominal_power = d.pop("nominal_power", UNSET)

        power = d.pop("power", UNSET)

        _energy = d.pop("energy", UNSET)
        energy: Union[Unset, InverterProduction]
        if isinstance(_energy, Unset):
            energy = UNSET
        else:
            energy = InverterProduction.from_dict(_energy)

        phase = []
        _phase = d.pop("phase", UNSET)
        for phase_item_data in _phase or []:
            phase_item = Phase.from_dict(phase_item_data)

            phase.append(phase_item)

        mppt = []
        _mppt = d.pop("mppt", UNSET)
        for mppt_item_data in _mppt or []:
            mppt_item = MPPT.from_dict(mppt_item_data)

            mppt.append(mppt_item)

        patched_inverter = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
            name=name,
            state=state,
            commission_date=commission_date,
            active=active,
            last_update=last_update,
            extended_state=extended_state,
            model_name=model_name,
            nominal_power=nominal_power,
            power=power,
            energy=energy,
            phase=phase,
            mppt=mppt,
        )

        patched_inverter.additional_properties = d
        return patched_inverter

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
