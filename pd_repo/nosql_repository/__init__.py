"""Module containing Interface and implementations for SQL-type
repositories."""
from ._base import AbstractNoSqlRepository
from ._fake import FakeNoSqlRepository
from ._mongo import MongoRepository

__all__ = ["AbstractNoSqlRepository", "MongoRepository", "FakeNoSqlRepository"]
