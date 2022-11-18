import typing as t
from dataclasses import dataclass


@dataclass
class User:
    id: int
    is_admin: bool

    @classmethod
    def get(cls, id: int) -> t.Optional['User']:
        # select * from user where id = $id; -> cls(...)
        return

    def save(self) -> 'User':
        # update user ... on conflict do nothig
        return self
