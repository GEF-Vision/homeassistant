import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.gateway_gateway_type import GatewayGatewayType
from ..models.gateway_state import GatewayState

T = TypeVar("T", bound="Gateway")


@attr.s(auto_attribs=True)
class Gateway:
    """
    Attributes:
        type (GatewayGatewayType): Type of the gateway. Possible choices are:<br>"alusta" = GEF Alusta<br>"reader" = GEF
            Reader
        serial_number (str):
        state (GatewayState): State of the device. Possible choices are:<br> 0: Offline<br> 1: Limited connectivity<br>
            2: Online<br>
        active (bool): Is the gateway activated?
        last_update (datetime.datetime): Time of last contact to GEF Vision.
        update_available (bool): Has the gateway available updates?
        update_progress (float): Update download progress in percentage.
        signal_strength (Optional[int]): Signal strength of the wireless connection. Possible values are:<br> null:
            wireless connection is not used<br> 0-100: strength expressed as percentage, where<br> 0-50: poor connectivity,
            51-75: good, 76-100: excellent
    """

    type: GatewayGatewayType
    serial_number: str
    state: GatewayState
    active: bool
    last_update: datetime.datetime
    update_available: bool
    update_progress: float
    signal_strength: Optional[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        serial_number = self.serial_number
        state = self.state.value

        active = self.active
        last_update = self.last_update.isoformat()

        update_available = self.update_available
        update_progress = self.update_progress
        signal_strength = self.signal_strength

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "serial_number": serial_number,
                "state": state,
                "active": active,
                "last_update": last_update,
                "update_available": update_available,
                "update_progress": update_progress,
                "signal_strength": signal_strength,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = GatewayGatewayType(d.pop("type"))

        serial_number = d.pop("serial_number")

        state = GatewayState(d.pop("state"))

        active = d.pop("active")

        last_update = isoparse(d.pop("last_update"))

        update_available = d.pop("update_available")

        update_progress = d.pop("update_progress")

        signal_strength = d.pop("signal_strength")

        gateway = cls(
            type=type,
            serial_number=serial_number,
            state=state,
            active=active,
            last_update=last_update,
            update_available=update_available,
            update_progress=update_progress,
            signal_strength=signal_strength,
        )

        gateway.additional_properties = d
        return gateway

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
