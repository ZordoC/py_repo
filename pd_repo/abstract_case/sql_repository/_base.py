"""Abstract base class for SQL type storage, Postgres, MySQL, SQLite ..."""
from abc import ABC, abstractmethod

import pandas as pd


class AbstractSqlRepository(ABC):
    """Interface for SQl type storage."""

    @abstractmethod
    def add(self, df: pd.DataFrame, table: str, if_exists: str) -> None:
        """Add dataframe to a table.

            df (pd.DataFrame): DataFrame to be added.
            table (str): Table to add DataFrame.
            if_exists (str): What to do if table exists, ie: append, fail.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, query: str) -> pd.DataFrame:
        """Get data from DB.

        Args:
            query (str): SQL query to get data from DB.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, query: str) -> pd.DataFrame:
        """Delete data from DB.

        Args:
            query (str): _description_

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        raise NotImplementedError
