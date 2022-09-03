"""Implementation of respository patter for MongoDB"""
from pymongo import MongoClient

from ._base import AbstractNoSqlRepository


class MongoRepository(AbstractNoSqlRepository):
    def __init__(self, conn_string: str, db: str):
        self._client = MongoClient(conn_string)
        self._db = self._client[db]
    
    def add(self, object: dict, collection: str) -> None:
        """Add dataframe to a table.

            df (pd.DataFrame): DataFrame to be added.
            table (str): Table to add DataFrame.
            if_exists (str): What to do if table exists, ie: append, fail.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        raise NotImplementedError

    def filter(self, filter: dict, collection: str) -> dict:
        """Get a subset from a collection.

        Args:
            query (str): SQL query to get data from DB.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        raise NotImplementedError

