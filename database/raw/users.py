from database.query import Query


def create_user_query(id_: int, name: str, tgusername: str, chatid: int, birthday: str = '', isadmin: int = 0) -> Query:
    bound_params = {
        'id': id_,
        'name': name,
        'tgusername': tgusername,
        'chatid': str(chatid),
        'birthday': birthday,
        'isadmin': isadmin,
    }

    query = Query(
        '''
        INSERT INTO user(id, name, tgusername, chatid, birthday, isadmin)
        VALUES(:id, :name, :tgusername, :chatid, :birthday, :isadmin)
        ON CONFLICT(id) DO UPDATE SET name=:name, tgusername=:tgusername, chatid=:chatid, birthday=:birthday, isadmin=:isadmin
        RETURNING id;
        ''',
        bound_params,
    )

    return query


def get_user_by_id_query(id_: int) -> Query:
    bound_params = {
        'id': id_
    }
    query = Query(
        '''
        SELECT id, name, tgusername, chatid, birthday, isadmin FROM user WHERE id=:id;
        ''',
        bound_params,
    )
 
    return query
