import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.override_status_overriden_output_state import OverrideStatusOverridenOutputState

T = TypeVar("T", bound="OverrideStatus")


@attr.s(auto_attribs=True)
class OverrideStatus:
    """
    Attributes:
        output_state (OverrideStatusOverridenOutputState): User-overriden output state of the control device. Possible
            choices are:<br> 0: Not supported (GEF Reader)<br> 1: Off<br> 2: On<br>
        start (datetime.datetime): Start time of the override period.
        end (datetime.datetime): End time of the override period.
    """

    output_state: OverrideStatusOverridenOutputState
    start: datetime.datetime
    end: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        output_state = self.output_state.value

        start = self.start.isoformat()

        end = self.end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "output_state": output_state,
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        output_state = OverrideStatusOverridenOutputState(d.pop("output_state"))

        start = isoparse(d.pop("start"))

        end = isoparse(d.pop("end"))

        override_status = cls(
            output_state=output_state,
            start=start,
            end=end,
        )

        override_status.additional_properties = d
        return override_status

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
