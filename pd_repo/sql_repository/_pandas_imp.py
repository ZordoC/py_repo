"""Implementation of repository pattern for SQLite database."""
import sqlite3

import pandas as pd

from ._base import AbstractSqlRepository


class PandasSqliteRepository(AbstractSqlRepository):
    """Concrete implementation of ``AbstractSqlRepository``"""

    def __init__(self, database_path: str):
        self._conn = sqlite3.connect(database_path)

    def get(self, query: str) -> pd.DataFrame:
        """Get data from table via pandas.

        Args:
            query (str): SQL query to execute.

        Returns:
            pd.DataFrame: Query result.
        """
        df = pd.read_sql(query, self._conn)
        return df.reset_index(drop=True).convert_dtypes()

    def add(self, df: pd.DataFrame, table: str, if_exists: str = "append") -> None:
        """Add a dataframe to a SQLite3 table.

        Args:
            df (pd.DataFrame): Dataframe to be added.
            table (str): Table to add data.
        """
        df.to_sql(table, self._conn, if_exists=if_exists, index=False)

    def delete(self, query: str) -> None:
        """Delete data using query.

        Args:
            query (str): Delete SQL query.
        """
        # TODO need condition to check if is DELETE query.
        self._conn.execute(query)
