"""Fake Implementation of repository pattern for SQL-type database used for
testing."""
import duckdb
import pandas as pd

from ._base import AbstractSqlRepository
from ._error import NotADeleteQuery, TableDoesNotExistError


class FakeSqlRepository(AbstractSqlRepository):
    """Fake implementation of a repository where tables are mocked using
    dataframes."""

    def __init__(self):
        self._table_integration = pd.DataFrame(
            columns=[
                "Age",
                "Number of sexual partners",
                "First sexual intercourse",
                "Num of pregnancies",
            ]
        )
        self._table_unit = pd.DataFrame(
            columns=["int_column", "date_column"],
        ).convert_dtypes()

        self.tables = {
            "table_integration": self._table_integration,
            "table_unit": self._table_unit,
        }

    def add(self, df: pd.DataFrame, table: str, if_exists: str = "append"):
        """Add dataframe to one of the existing dataframes.

        Args:
            df (pd.DataFrame): _description_
            table (str): _description_
            if_exists (str, optional): _description_. Defaults to "append".

        Raises:
            NotImplementedError: When ``if_exists`` is not append.
            TableDoesNotExistError: Raised when table does not exist.
        """
        if if_exists != "append":
            raise NotImplementedError("Fake only has append implementation.")
        try:
            self.tables[table] = pd.concat([self.tables[table], df]).convert_dtypes()
        except KeyError as exc:
            raise TableDoesNotExistError("Table does not exist") from exc

    def delete(self, query: str):
        """Reset our "table" dataframes."""
        if "DELETE".lower() not in query.lower():
            raise NotADeleteQuery("It's not a delete query")
        self.tables["table_unit"] = pd.DataFrame(columns=["int_column", "date_column"])
        self.tables["table_integration"] = pd.DataFrame(
            columns=[
                "Age",
                "Number of sexual partners",
                "First sexual intercourse",
                "Num of pregnancies",
            ]
        )

    def get(self, query: str):
        """Get data via duckdub from one of the dataframes initialized."""
        # necessary for duckdb
        # pylint: disable=W0612
        # pylint: disable=I1101
        table_unit = self.tables["table_unit"]  # noqa: F841
        table_integration = self.tables["table_integration"]  # noqa: F841
        return duckdb.query(query).df().convert_dtypes()
