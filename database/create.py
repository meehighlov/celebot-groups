import sqlite3

from database.session import session
from database.query import Query


create_user_table = '''
CREATE TABLE IF NOT EXISTS user (
		id INTEGER PRIMARY KEY,
		name VARCHAR,
		tgusername VARCHAR,
		chatid VARCHAR,
		birthday VARCHAR,
		isadmin INTEGER
	);
'''


def rollout():
    with session() as s:
        s.execute(Query(create_user_table))
