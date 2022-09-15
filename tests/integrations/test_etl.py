"""Testing using fakes."""
import pytest

from pd_repo.scripts.example import DATASET, extract, load, transform
from pd_repo.sql_repository import FakeSqlRepository


@pytest.fixture()
def raw_df():
    df = extract(DATASET)
    return df

def test_extract(raw_df):
    assert not raw_df.empty
    assert len(raw_df) > 1

def test_transform(raw_df):
    df_final = transform(raw_df)
    assert len(df_final.columns) == 4


def test_load(test_df_integration):
    fake_repo = FakeSqlRepository()
    load(test_df_integration, fake_repo, "table_integration")
    res = fake_repo.get("SELECT * FROM 'table_integration'")
    assert res.equals(test_df_integration)





