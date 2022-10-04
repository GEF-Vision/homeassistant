from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="State")


@attr.s(auto_attribs=True)
class State:
    """
    Attributes:
        state_code (int): State code as integer.
        description (str): State code description.
    """

    state_code: int
    description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state_code = self.state_code
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state_code": state_code,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        state_code = d.pop("state_code")

        description = d.pop("description")

        state = cls(
            state_code=state_code,
            description=description,
        )

        state.additional_properties = d
        return state

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
