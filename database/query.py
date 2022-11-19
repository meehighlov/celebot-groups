import typing as t


class Query:
    def __init__(self, raw_sql: str, params: dict[str, t.Union[int, str]] = None) -> None:
        self.raw_sql = raw_sql
        self.params = params
