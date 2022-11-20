import sqlite3
from app.config import config
from database.query import Query


class session:

    def __init__(self, db_name: str = None) -> None:
        db_name = db_name or config.APP_NAME + '.db'
        self.connection = sqlite3.connect(db_name)

    def execute(self, query: Query, many: bool = False, commit: bool = False) -> sqlite3.Cursor:
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)

        cur = self.connection.cursor()
        strategy = cur.executemany if many else cur.execute

        result = None

        if query.params:
            result = strategy(query.raw_sql, query.params)
        else:
            result = strategy(query.raw_sql)

        if commit:
            self.commit()
            return result

        return result

    def close_connection(self):
        self.connection.close()
        self.connection = None

    def commit(self) -> None:
        self.connection.commit()
        self.close_connection()

    def rollback(self) -> None:
        self.connection.rollback()
        self.close_connection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
            return

        self.commit()
