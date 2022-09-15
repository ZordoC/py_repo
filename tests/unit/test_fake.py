"""Unit test for SqlRepository."""
import pandas as pd
import pytest

from pd_repo.sql_repository import FakeSqlRepository


@pytest.fixture()
def fake_repo():
    return FakeSqlRepository()


def test_add(fake_repo, test_df):
    fake_repo.add(test_df, "table_unit", "append")
    print(fake_repo.table_unit)
    assert fake_repo.table_unit.equals(test_df)


def test_get(fake_repo, test_df):
    fake_repo.add(test_df, "table_unit", "append")
    res = fake_repo.get("SELECT * FROM 'table_unit'")
    print(res)
    assert res.equals(test_df)


def test_delete(fake_repo, test_df):
    fake_repo.add(test_df, "table_unit", "append")
    assert not fake_repo.table_unit.empty
    fake_repo.delete("DELETE FROM table_unit;")
    assert fake_repo.table_unit.empty
