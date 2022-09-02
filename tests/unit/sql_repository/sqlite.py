"""Unit test for SqliteRepository."""
import pandas as pd
import pytest

from pd_repo.sql_repository import SqliteRepository

TABLE = "test_table"


@pytest.fixture()
def test_df():
    """Dataframe for testing."""
    df = pd.DataFrame(
        data=[[0, "10/11/12"], [1, "12/11/10"]], columns=["int_column", "date_column"]
    )
    return df


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
    repo.add(test_df, TABLE, if_exists="append")
    SQL = f"SELECT * FROM {TABLE}"

    df = repo.get(SQL)
    comparisson = pd.concat([test_df, test_df]).reset_index(drop=True)

    assert df.equals(comparisson)


def test_drop_table(repo):
    """Drops table at the end of unit-testing."""
    SQL = f"""DROP TABLE {TABLE};"""
    repo._conn.execute(SQL)
