"""Interface for No-SQL-type respositories"""
from abc import abstractmethod, ABC

import pandas as pd


class AbstractNoSqlRepository(ABC):

    @abstractmethod
    def add(self, df: pd.DataFrame, collection: str) -> None:
        """Add dataframe to a table.

            df (pd.DataFrame): DataFrame to be added.
            table (str): Table to add DataFrame.
            if_exists (str): What to do if table exists, ie: append, fail.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        raise NotImplementedError

    @abstractmethod
    def filter(self, filter: dictionary, collection: str) -> pd.DataFrame:
        """Get data from DB.

        Args:
            query (str): SQL query to get data from DB.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        raise NotImplementedError
