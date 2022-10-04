from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.device_gateway_type import DeviceGatewayType

T = TypeVar("T", bound="DeviceGateway")


@attr.s(auto_attribs=True)
class DeviceGateway:
    """
    Attributes:
        type (DeviceGatewayType):
        serial_number (str):
    """

    type: DeviceGatewayType
    serial_number: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        serial_number = self.serial_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "serial_number": serial_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DeviceGatewayType(d.pop("type"))

        serial_number = d.pop("serial_number")

        device_gateway = cls(
            type=type,
            serial_number=serial_number,
        )

        device_gateway.additional_properties = d
        return device_gateway

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
