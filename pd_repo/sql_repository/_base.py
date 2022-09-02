"""Abstract base class for SQL type storage, Postgres, MySQL, SQLite ..."""
from abc import ABC, abstractmethod

import pandas as pd


class AbstractSqlRepository(ABC):
    """Interface for SQl type storage."""

    @abstractmethod
    def add(self, df: pd.DataFrame, table: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, query: str) -> pd.DataFrame:
        raise NotImplementedError
