"""Unit test for MongoRepository"""
import pandas as pd
import pytest

from pd_repo.nosql_repository import SqliteRepository

TABLE = "test_table"


@pytest.fixture()
def repo():
    return SqliteRepository("test.db")