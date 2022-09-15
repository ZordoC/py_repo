"""Fake Implementation of repository pattern for SQL-type database used for
testing."""
import sqlite3

import duckdb
import pandas as pd

from ._base import AbstractSqlRepository
from ._error import NotADeleteQuery


class FakeSqlRepository(AbstractSqlRepository):
    def __init__(self):
        self.table_integration = pd.DataFrame(
            columns=[
                "Age",
                "Number of sexual partners",
                "First sexual intercourse",
                "Num of pregnancies",
            ]
        )
        self.table_unit = df = pd.DataFrame(
            columns=["int_column", "date_column"],
        ).convert_dtypes()

    def add(self, df: pd.DataFrame, table: str, if_exists: str):
        if if_exists == "append":
            if table == "table_unit":
                self.table_unit = pd.concat([self.table_unit, df]).convert_dtypes()
            if table == "table_integration":
                self.table_integration = pd.concat(
                    [self.table_integration, df]
                ).convert_dtypes()
        else:
            raise NotImplementedError("Only append exists in fake.")

    def delete(self, query: str):
        if "DELETE".lower() not in query.lower():
            raise NotADeleteQuery("It's not a delete query")
        self.table_unit = pd.DataFrame(columns=["int_column", "date_column"])
        self.table_integration = pd.DataFrame(
            columns=[
                "Age",
                "Number of sexual partners",
                "First sexual intercourse",
                "Num of pregnancies",
            ]
        )

    def get(self, query: str):
        table_unit = self.table_unit  # For duckdb to access
        table_integration = self.table_integration
        return duckdb.query(query).df().convert_dtypes()
