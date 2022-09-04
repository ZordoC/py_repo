"""Module containing Interface and implementations for SQL-type
repositories."""
from ._base import AbstractSqlRepository
from ._fake import FakeSqlRepository
from ._pandas_imp import PandasSqliteRepository
from ._sqlite3_imp import Sqlite3Repository


__all__ = [
    "AbstractSqlRepository",
    "FakeSqlRepository",
    "Sqlite3Repository",
    "PandasSqliteRepository",
]
