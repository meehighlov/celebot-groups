import typing as t
from dataclasses import asdict, dataclass


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

    @property
    def birth_day(self) -> t.Optional[str]:
        if self.birthday != '':
            return self.birthday
    
    def as_dict(self) -> dict:
        return asdict(self)
