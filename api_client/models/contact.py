from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="Contact")


@attr.s(auto_attribs=True)
class Contact:
    """
    Attributes:
        name (str): Name of the company.
        address (Optional[str]): Address of the company.
        website (Optional[str]): Website of the company.
        phone_number (Optional[str]): Phone number for support.
        email (Optional[str]): Email address for support.
        logo (Optional[str]): URL for the company logo.
    """

    name: str
    address: Optional[str]
    website: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    logo: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address = self.address
        website = self.website
        phone_number = self.phone_number
        email = self.email
        logo = self.logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
                "website": website,
                "phone_number": phone_number,
                "email": email,
                "logo": logo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        address = d.pop("address")

        website = d.pop("website")

        phone_number = d.pop("phone_number")

        email = d.pop("email")

        logo = d.pop("logo")

        contact = cls(
            name=name,
            address=address,
            website=website,
            phone_number=phone_number,
            email=email,
            logo=logo,
        )

        contact.additional_properties = d
        return contact

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
