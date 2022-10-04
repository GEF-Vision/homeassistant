import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.inverter_device_type import InverterDeviceType
from ..models.inverter_extended_state import InverterExtendedState
from ..models.inverter_production import InverterProduction
from ..models.inverter_state import InverterState
from ..models.mppt import MPPT
from ..models.phase import Phase
from ..types import UNSET, Unset

T = TypeVar("T", bound="Inverter")


@attr.s(auto_attribs=True)
class Inverter:
    """
    Attributes:
        gateway (DeviceGateway):
        device_type (InverterDeviceType): Device type
        id (int): Unique (per device-type) identifier of the device.
        state (InverterState): State of the device. Possible choices are:<br> 0: Error<br> 1: Warning<br> 2: OK<br>
        commission_date (datetime.date): Date when the device was commissioned.
        active (bool): Is the device active? Devices can become inactive for example when exchanged to a new one.
        last_update (datetime.datetime): Time of last update for device measurements.
        extended_state (InverterExtendedState): Extended state of the inverter. Possible choices are:<br> 0: Unknown<br>
            1: Off<br> 2: Sleep<br> 3: Starting<br> 4: Run<br> 5: Throttle<br> 6: Shutting down<br> 7: Fault<br> 8:
            Standby<br> 9: Warning<br> 10: Read error<br> 11: No production in 24 hours<br> 12: No communication in 24
            hours<br>
        model_name (str): Model name of the inverter.
        nominal_power (int): Nominal power of the inverter in watts (W).
        power (int): Inverter active power in watts (W).
        energy (InverterProduction):
        phase (List[Phase]): Measurements for AC phases.
        mppt (List[MPPT]): Measurements for MPPT trackers.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
    """

    gateway: DeviceGateway
    device_type: InverterDeviceType
    id: int
    state: InverterState
    commission_date: datetime.date
    active: bool
    last_update: datetime.datetime
    extended_state: InverterExtendedState
    model_name: str
    nominal_power: int
    power: int
    energy: InverterProduction
    phase: List[Phase]
    mppt: List[MPPT]
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

        extended_state = self.extended_state.value

        model_name = self.model_name
        nominal_power = self.nominal_power
        power = self.power
        energy = self.energy.to_dict()

        phase = []
        for phase_item_data in self.phase:
            phase_item = phase_item_data.to_dict()

            phase.append(phase_item)

        mppt = []
        for mppt_item_data in self.mppt:
            mppt_item = mppt_item_data.to_dict()

            mppt.append(mppt_item)

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
                "extended_state": extended_state,
                "model_name": model_name,
                "nominal_power": nominal_power,
                "power": power,
                "energy": energy,
                "phase": phase,
                "mppt": mppt,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gateway = DeviceGateway.from_dict(d.pop("gateway"))

        device_type = InverterDeviceType(d.pop("device_type"))

        id = d.pop("id")

        state = InverterState(d.pop("state"))

        commission_date = isoparse(d.pop("commission_date")).date()

        active = d.pop("active")

        last_update = isoparse(d.pop("last_update"))

        extended_state = InverterExtendedState(d.pop("extended_state"))

        model_name = d.pop("model_name")

        nominal_power = d.pop("nominal_power")

        power = d.pop("power")

        energy = InverterProduction.from_dict(d.pop("energy"))

        phase = []
        _phase = d.pop("phase")
        for phase_item_data in _phase:
            phase_item = Phase.from_dict(phase_item_data)

            phase.append(phase_item)

        mppt = []
        _mppt = d.pop("mppt")
        for mppt_item_data in _mppt:
            mppt_item = MPPT.from_dict(mppt_item_data)

            mppt.append(mppt_item)

        name = d.pop("name", UNSET)

        inverter = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
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
            name=name,
        )

        inverter.additional_properties = d
        return inverter

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
