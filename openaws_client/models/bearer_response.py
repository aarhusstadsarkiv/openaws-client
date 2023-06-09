from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BearerResponse")


@attr.s(auto_attribs=True)
class BearerResponse:
    """
    Attributes:
        access_token (str):
        token_type (str):
    """

    access_token: str
    token_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        token_type = self.token_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "token_type": token_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token")

        token_type = d.pop("token_type")

        bearer_response = cls(
            access_token=access_token,
            token_type=token_type,
        )

        bearer_response.additional_properties = d
        return bearer_response

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
