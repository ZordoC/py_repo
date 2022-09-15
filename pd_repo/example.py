"""Example script to test out the pattern"""
import warnings

import pandas as pd
import re
from sql_repository import AbstractSqlRepository, Sqlite3Repository, PandasSqliteRepository


DATASET = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv'


def extract(url: str) -> pd.DataFrame:
    """Get data from internet (url), return dataframe."""
    df = pd.read_csv(url)
    df = df[(df != '?').all(axis=1)]
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transform data"""
    df = df.iloc[:, [0, 1, 2, 3]]
    columns = list(df.columns)
    for col in columns:
        df[col] = df[col].apply(lambda x: (float(x)))
    return df

def load(df, repo: AbstractSqlRepository, table: str):
    """Load data to a SQLite database."""
    repo.add(df, table)

    
def etl(url, repo: AbstractSqlRepository, table: str):
    """Extract, Transform, Load."""
    df = extract(url)
    df = transform(df)
    df = load(df, repo, table)

    

if __name__ == "__name__":

    print("Jose")

    repo = Sqlite3Repository("main_db.db")
    
    df_raw = extract(DATASET)

    df_final = transform(df_raw)

    df_check = repo.get("SELECT * FROM anna_test")

    assert df_check == df_final

    print("Hey")
