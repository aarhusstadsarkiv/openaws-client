from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_flag import UserFlag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_read_data import UserReadData
    from ..models.user_roles import UserRoles


T = TypeVar("T", bound="UserRead")


@attr.s(auto_attribs=True)
class UserRead:
    """Base User model.

    Attributes:
        email (str):
        data (UserReadData):
        roles (UserRoles):
        flags (UserFlag): To check if a user has a flag, use bitmasking:
            >>> assert user.flags & UserFlag.EMPLOYEE
            Add a flag:
            >>> user.flags |= UserFlag.EMPLOYEE
            Remove a flag:
            >>> user.flags &= ~UserFlag.EMPLOYEE

            Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.
        id (Union[Unset, Any]):
        is_active (Union[Unset, bool]):  Default: True.
        is_superuser (Union[Unset, bool]):
        is_verified (Union[Unset, bool]):
    """

    email: str
    data: "UserReadData"
    roles: "UserRoles"
    flags: UserFlag
    id: Union[Unset, Any] = UNSET
    is_active: Union[Unset, bool] = True
    is_superuser: Union[Unset, bool] = False
    is_verified: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        data = self.data.to_dict()

        roles = self.roles.to_dict()

        flags = self.flags.value

        id = self.id
        is_active = self.is_active
        is_superuser = self.is_superuser
        is_verified = self.is_verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "data": data,
                "roles": roles,
                "flags": flags,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_read_data import UserReadData
        from ..models.user_roles import UserRoles

        d = src_dict.copy()
        email = d.pop("email")

        data = UserReadData.from_dict(d.pop("data"))

        roles = UserRoles.from_dict(d.pop("roles"))

        flags = UserFlag(d.pop("flags"))

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        user_read = cls(
            email=email,
            data=data,
            roles=roles,
            flags=flags,
            id=id,
            is_active=is_active,
            is_superuser=is_superuser,
            is_verified=is_verified,
        )

        user_read.additional_properties = d
        return user_read

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
