#!/usr/bin/env python
"""Conftest for `pd_repo` package."""
import pandas as pd
import pytest
import requests



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
    )
    return df
