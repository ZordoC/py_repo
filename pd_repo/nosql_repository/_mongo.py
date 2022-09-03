"""Implementation of respository patter for MongoDB."""
from pymongo import MongoClient

from ._base import AbstractNoSqlRepository


class MongoRepository(AbstractNoSqlRepository):
    def __init__(self, conn_string: str, db: str):
        self._client = MongoClient(conn_string)
        self._db = self._client[db]

    def insert_one(self, document: dict, collection: str) -> None:
        """Add dataframe to a table.

            df (pd.DataFrame): DataFrame to be added.
            table (str): Table to add DataFrame.
            if_exists (str): What to do if table exists, ie: append, fail.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        coll = self._db[collection]
        coll.insert_one(document)

    def find(self, query: dict, collection: str, filter: dict = {}) -> dict:
        """Get a subset from a collection.

        Args:
            query (str): SQL query to get data from DB.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        coll = self._db[collection]
        return coll.find(query, filter)

    def list_all(self, collection: str) -> list:
        """List all documents from a collection.

        Args:
            collection (str): String collection.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        coll = self._db[collection]
        return coll
