"""Module containing Interface and implementations for SQL-type repositories."""
from ._base import AbstractSqlRepository
from ._sqlite_imp import SqliteRepository

__all__ = ["AbstractSqlRepository", "SqliteRepository"]
