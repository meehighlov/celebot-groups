import typing as t
from database.session import session


from database.models import User
from database.raw.users import create_user_query, get_all_users_query, get_user_by_id_query


def get_user_by_id(user_id: int) -> t.Optional[User]:
    q = get_user_by_id_query(user_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return User(*r)


def save_user(**kwargs) -> int:
    q = create_user_query(**kwargs)
    with session() as s:
        r = s.execute(q).fetchone()
        return r[0]


def get_all_users() -> list[User]:
    q = get_all_users_query()
    users = []
    with session() as s:
        for user in s.execute(q):
            users.append(User(*user))
        return users
