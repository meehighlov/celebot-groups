import typing as t
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str 
    tgusername: str
    chatid: str
    birthday: str
    isadmin: int

    @property
    def is_admin(self):
        return self.isadmin == 1
