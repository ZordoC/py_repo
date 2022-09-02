import sqlite3

import pandas as pd

from ._base import AbstractSqlRepository


class SqliteRepository(AbstractSqlRepository):
    def __init__(self, database_path: str):
        self._conn = sqlite3.connect(database_path)

    def get(self, query: str) -> pd.DataFrame:
        """Get data from table via pandas.

        Args:
            query (str): _description_

        Returns:
            pd.DataFrame: _description_
        """
        df = pd.read_sql(query, self._conn)
        df = df.drop(columns=["index"], axis=0)
        return df.reset_index(drop=True)

    def add(self, df: pd.DataFrame, table: str, if_exists: str = "append"):
        """_summary_

        Args:
            df (pd.DataFrame): _description_
            table (str): _description_
        """
        df.to_sql(table, self._conn, if_exists=if_exists)
