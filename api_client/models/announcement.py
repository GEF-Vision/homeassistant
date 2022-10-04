import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Announcement")


@attr.s(auto_attribs=True)
class Announcement:
    """
    Attributes:
        start_date (datetime.date): Start date of the period when the announcement should be shown.
        end_date (datetime.date): End date of the period when the announcement should be shown.
        title (str): Announcement title.
        text (str): Announcement text body.
        image (Union[Unset, str]): URL of the image attached to the announcement. Default: ''.
        link (Union[Unset, str]): URL the announcement links to. Default: ''.
        link_text (Union[Unset, str]): Text to use in the link. Default: ''.
    """

    start_date: datetime.date
    end_date: datetime.date
    title: str
    text: str
    image: Union[Unset, str] = ""
    link: Union[Unset, str] = ""
    link_text: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date = self.start_date.isoformat()
        end_date = self.end_date.isoformat()
        title = self.title
        text = self.text
        image = self.image
        link = self.link
        link_text = self.link_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_date": start_date,
                "end_date": end_date,
                "title": title,
                "text": text,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if link is not UNSET:
            field_dict["link"] = link
        if link_text is not UNSET:
            field_dict["link_text"] = link_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        title = d.pop("title")

        text = d.pop("text")

        image = d.pop("image", UNSET)

        link = d.pop("link", UNSET)

        link_text = d.pop("link_text", UNSET)

        announcement = cls(
            start_date=start_date,
            end_date=end_date,
            title=title,
            text=text,
            image=image,
            link=link,
            link_text=link_text,
        )

        announcement.additional_properties = d
        return announcement

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
