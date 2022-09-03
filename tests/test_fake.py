"""Unit test for SqlRepository."""
import pandas as pd
import pytest

from pd_repo.sql_repository import FakeSqlRepository


@pytest.fixture()
def fake_repo():
    return FakeSqlRepository()


def test_add(fake_repo, test_df):
    fake_repo.add(test_df, "table_1", "append")
    assert fake_repo.table_1.equals(test_df)


def test_get(fake_repo, test_df):
    fake_repo.add(test_df, "table_1", "append")
    res = fake_repo.get("SELECT * FROM 'table_1'")
    assert res.equals(test_df)


def test_delete(fake_repo, test_df):
    fake_repo.add(test_df, "table_1", "append")
    assert not fake_repo.table_1.empty
    fake_repo.delete("DELETE FROM table_1;")
    assert fake_repo.table_1.empty
