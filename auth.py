from database.ext.users import get_user_by_id


def is_auth_user(user_id: int) -> bool:
    user = get_user_by_id(user_id)
    return user is not None

