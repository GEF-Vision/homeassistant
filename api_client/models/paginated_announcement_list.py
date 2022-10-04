from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.announcement import Announcement
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginatedAnnouncementList")


@attr.s(auto_attribs=True)
class PaginatedAnnouncementList:
    """
    Attributes:
        next_ (Union[Unset, None, str]):
        previous (Union[Unset, None, str]):
        results (Union[Unset, List[Announcement]]):
    """

    next_: Union[Unset, None, str] = UNSET
    previous: Union[Unset, None, str] = UNSET
    results: Union[Unset, List[Announcement]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_ = self.next_
        previous = self.previous
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = Announcement.from_dict(results_item_data)

            results.append(results_item)

        paginated_announcement_list = cls(
            next_=next_,
            previous=previous,
            results=results,
        )

        paginated_announcement_list.additional_properties = d
        return paginated_announcement_list

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
