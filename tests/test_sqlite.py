"""Unit test for SqliteRepository."""
import pandas as pd
import pytest

from pd_repo.sql_repository import SqliteRepository

TABLE = "test_table"


@pytest.fixture()
def repo():
    return SqliteRepository("test.db")


def test_get_data(repo, test_df):
    """Test for repo.get method."""
    repo.add(test_df, TABLE)
    SQL = f"SELECT * FROM {TABLE}"
    df = repo.get(SQL)
    assert df.equals(test_df)


def test_append_to_table(repo, test_df):
    """Test for appending dataframe to a table."""
    repo.add(test_df, TABLE)
    SQL = f"SELECT * FROM {TABLE}"

    df = repo.get(SQL)
    comparisson = pd.concat([test_df, test_df]).reset_index(drop=True).convert_dtypes()

    assert df.equals(comparisson)


def test_drop_table(repo):
    """Drops table at the end of unit-testing."""
    SQL = f"""DROP TABLE {TABLE};"""
    repo._conn.execute(SQL)
