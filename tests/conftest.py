#!/usr/bin/env python
"""Conftest for `pd_repo` package."""
import pandas as pd
import pytest
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, clear_mappers, sessionmaker

from pd_repo.domain_case.service_layer import metadata, start_mappers


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return requests.get("https://github.com/audreyr/cookiecutter-pypackage")


@pytest.fixture()
def test_df():
    """Dataframe for testing."""
    df = pd.DataFrame(
        data=[[0, "10/11/12"], [1, "12/11/10"]], columns=["int_column", "date_column"]
    ).convert_dtypes()
    return df


@pytest.fixture()
def test_df_integration():
    """Dataframe for testing."""
    df = pd.DataFrame(
        data=[[41, 3, 17, 4], [32, 1, 18, 1]],
        columns=[
            "Age",
            "Number of sexual partners",
            "First sexual intercourse",
            "Num of pregnancies",
        ],
    ).convert_dtypes()
    return df


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def domain_session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()
