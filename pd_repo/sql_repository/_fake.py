"""Fake Implementation of repository pattern for SQL-type database used for
testing."""
import sqlite3

import duckdb
import pandas as pd

from ._base import AbstractSqlRepository
from ._error import NotADeleteQuery


class FakeSqlRepository(AbstractSqlRepository):
    def __init__(self):
        self.table_1 = pd.DataFrame(columns=["int_column", "date_column"])

    def add(self, df: pd.DataFrame, table: str, if_exists: str):
        if if_exists == "append":
            self.table_1 = pd.concat([self.table_1, df]).convert_dtypes()
        else:
            raise NotImplementedError

    def delete(self, query: str):
        table_1 = self.table_1  # For duckdb to access
        if "DELETE".lower() not in query.lower():
            raise NotADeleteQuery("It's not a delete query")
        self.table_1 = pd.DataFrame(columns=["int_column", "date_column"])

    def get(self, query: str):
        table_1 = self.table_1  # For duckdb to access
        return duckdb.query(query).df().convert_dtypes()
