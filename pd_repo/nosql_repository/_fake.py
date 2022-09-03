"""Fake Implementation for testing"""
from ._base import AbstractNoSqlRepository


class FakeNoSqlRepository(AbstractNoSqlRepository):
    def __init__(self):
        self._db = {"collection_1": [], "collection_2": []}

    def insert_one(self, document: dict, collection: str) -> None:
        """Add dataframe to a table. (Mock)

            df (pd.DataFrame): DataFrame to be added.
            table (str): Table to add DataFrame.
            if_exists (str): What to do if table exists, ie: append, fail.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        self._db[collection].append(document)

    def find(self, query: dict, collection: str, filter: dict = {}) -> dict:
        """Mock method, will always return the same object.

        Args:
            query (str): SQL query to get data from DB.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        return {"name": "jose", "age": 25}

    def list_all(self, collection: str) -> dict:
        """List all documents from a collection.

        Args:
            query (str): SQL query to get data from DB.

        Raises:
            NotImplementedError: Abstract methods don't have implementation.
        """
        coll = self._db[collection]
        return coll