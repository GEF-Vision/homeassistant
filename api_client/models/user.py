from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.contact import Contact

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        username (str): Username of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        email (str): Email address of the user.
        company (Optional[Contact]):
    """

    username: str
    first_name: str
    last_name: str
    email: str
    company: Optional[Contact]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        company = self.company.to_dict() if self.company else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "company": company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        _company = d.pop("company")
        company: Optional[Contact]
        if _company is None:
            company = None
        else:
            company = Contact.from_dict(_company)

        user = cls(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company,
        )

        user.additional_properties = d
        return user

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
