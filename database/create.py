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

def rollout(db_name: str):
    pass
