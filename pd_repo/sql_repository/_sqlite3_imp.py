"""Implementation of repository pattern for SQLite database."""
import sqlite3

import pandas as pd

from ._base import AbstractSqlRepository


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
        results = self._cursor.execute(query)
        return df.reset_index(drop=True).convert_dtypes()

    def add(self, df: pd.DataFrame, table: str, if_exists: str = "append") -> None:
        """_summary_

        Args:
            df (pd.DataFrame): _description_
            table (str): _description_
        """
        df.to_sql(table, self._conn, if_exists=if_exists)

    def delete(self, query: str) -> None:
        """_summary_

        Args:
            query (str): _description_

        Returns:
            pd.DataFrame: _description_
        """
        # TODO need condition to check if is DELETE query.
        self._conn.execute(query)
