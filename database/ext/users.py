import typing as t


from database.models import User


def get_user_by_id(user_id: int) -> t.Optional[User]:
    return User.get(user_id)
