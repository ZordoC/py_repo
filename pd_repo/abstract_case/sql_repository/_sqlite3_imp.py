"""Implementation of repository pattern for SQLite database."""
import re
import sqlite3

import pandas as pd

from ._base import AbstractSqlRepository
from ._error import NotADeleteQuery


class Sqlite3Repository(AbstractSqlRepository):
    """Concrete implementation of ``AbstractSqlRepository``"""

    def __init__(self, database_path: str):
        self._conn = sqlite3.connect(database_path)

    def get(self, query: str) -> pd.DataFrame:
        """Get data from table via sqlite3 cursor.

        Args:
            query (str): Query to be executed

        Returns:
            pd.DataFrame: Query result.
        """
        cursor = self._conn.cursor()
        results = cursor.execute(query)
        columns = [i[0] for i in cursor.description]
        data = results.fetchall()
        return self._convert_to_dataframe(data, columns)

    def add(self, df: pd.DataFrame, table: str, if_exists: str = "append") -> None:
        """Add a dataframe using sqlite3 engine.

        Args:
            df (pd.DataFrame): Dataframe to be added to DB.
            table (str): Table of the SQLite database.
        """
        cur = self._conn.cursor()
        data = df.to_records(index=False)
        number_of_columns = len(data[0])
        dynamic_value_string = self._get_into_values_string(number_of_columns)
        try:
            cur.executemany(f"INSERT INTO {table} VALUES{dynamic_value_string}", data)
        except sqlite3.OperationalError:
            columns = str(tuple(df.columns))
            cur.execute(f"CREATE TABLE {table}{columns}")
        finally:
            cur.executemany(f"INSERT INTO {table} VALUES{dynamic_value_string}", data)

        self._conn.commit()

    @staticmethod
    def _get_into_values_string(length: int):
        string = "(" + ",?" * length + ")"
        string = re.sub(",", "", string, 1)
        return string

    def delete(self, query: str) -> None:
        """Delete certain asset from a database.

        Args:
            query (str): DELETE SQL query.
        """
        if "DELETE".lower() not in query.lower():
            raise NotADeleteQuery("It's not a delete query")
        self._conn.execute(query)

    def _convert_to_dataframe(self, data: list, columns: str):
        return pd.DataFrame(data, columns=columns).convert_dtypes().reset_index(drop=True)
