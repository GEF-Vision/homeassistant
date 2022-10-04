import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_gateway import DeviceGateway
from ..models.energymeter_device_type import EnergymeterDeviceType
from ..models.energymeter_energy import EnergymeterEnergy
from ..models.energymeter_meter_type import EnergymeterMeterType
from ..models.energymeter_phase import EnergymeterPhase
from ..models.energymeter_power import EnergymeterPower
from ..models.energymeter_state import EnergymeterState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Energymeter")


@attr.s(auto_attribs=True)
class Energymeter:
    """
    Attributes:
        gateway (DeviceGateway):
        device_type (EnergymeterDeviceType): Device type
        id (int): Unique (per device-type) identifier of the device.
        state (EnergymeterState): State of the device. Possible choices are:<br> 0: Error<br> 1: Warning<br> 2: OK<br>
        commission_date (datetime.date): Date when the device was commissioned.
        active (bool): Is the device active? Devices can become inactive for example when exchanged to a new one.
        last_update (datetime.datetime): Time of last update for device measurements.
        meter_type (EnergymeterMeterType): Type of the energymeter. Possible values are: <br> 0: Grid interface<br> 1:
            Consumption<br> 2: Production<br>
        power (EnergymeterPower):
        energy (EnergymeterEnergy):
        phase (List[EnergymeterPhase]): Measurements for AC phases.
        name (Union[Unset, str]): Name of the device (optional). Default: ''.
    """

    gateway: DeviceGateway
    device_type: EnergymeterDeviceType
    id: int
    state: EnergymeterState
    commission_date: datetime.date
    active: bool
    last_update: datetime.datetime
    meter_type: EnergymeterMeterType
    power: EnergymeterPower
    energy: EnergymeterEnergy
    phase: List[EnergymeterPhase]
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

        meter_type = self.meter_type.value

        power = self.power.to_dict()

        energy = self.energy.to_dict()

        phase = []
        for phase_item_data in self.phase:
            phase_item = phase_item_data.to_dict()

            phase.append(phase_item)

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
                "meter_type": meter_type,
                "power": power,
                "energy": energy,
                "phase": phase,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gateway = DeviceGateway.from_dict(d.pop("gateway"))

        device_type = EnergymeterDeviceType(d.pop("device_type"))

        id = d.pop("id")

        state = EnergymeterState(d.pop("state"))

        commission_date = isoparse(d.pop("commission_date")).date()

        active = d.pop("active")

        last_update = isoparse(d.pop("last_update"))

        meter_type = EnergymeterMeterType(d.pop("meter_type"))

        power = EnergymeterPower.from_dict(d.pop("power"))

        energy = EnergymeterEnergy.from_dict(d.pop("energy"))

        phase = []
        _phase = d.pop("phase")
        for phase_item_data in _phase:
            phase_item = EnergymeterPhase.from_dict(phase_item_data)

            phase.append(phase_item)

        name = d.pop("name", UNSET)

        energymeter = cls(
            gateway=gateway,
            device_type=device_type,
            id=id,
            state=state,
            commission_date=commission_date,
            active=active,
            last_update=last_update,
            meter_type=meter_type,
            power=power,
            energy=energy,
            phase=phase,
            name=name,
        )

        energymeter.additional_properties = d
        return energymeter

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
