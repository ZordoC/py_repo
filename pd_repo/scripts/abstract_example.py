"""Example script to test out the pattern."""
import argparse
import random
import string
import warnings

import pandas as pd

from pd_repo.abstract_case.sql_repository import (
    AbstractSqlRepository,
    PandasSqliteRepository,
    Sqlite3Repository,
)

warnings.filterwarnings("ignore")


DATASET = "https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv"  # pylint: disable=C0301


def get_random_string(length):
    """Returns a random string with combination of lower and upper case."""
    result_str = "".join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


def extract(url: str) -> pd.DataFrame:
    """Get data from internet (url), return dataframe."""
    df = pd.read_csv(url)
    df = df[(df != "?").all(axis=1)]
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transform data."""
    df = df.iloc[:, [0, 1, 2, 3]]
    columns = list(df.columns)
    for col in columns:
        df[col] = df[col].astype(float)
    return df


def load(df, repo: AbstractSqlRepository, table: str):
    """Load data to a SQLite database."""
    repo.add(df, table)


if __name__ == "__main__":

    # Parsing arguments for example script.
    parser = argparse.ArgumentParser()
    parser.add_argument("db_name", help="Name of Sqlite database", default="main_db")
    parser.add_argument(
        "--use-pandas",
        help="Uses Pandas repository to interact with SQLite database",
        action="store_true",
    )
    args = parser.parse_args()

    if args.use_pandas:
        sql_repo = PandasSqliteRepository(args.db_name)
    else:
        sql_repo = Sqlite3Repository(args.db_name)

    # for testing purposes we create a random table
    table_name = get_random_string(4)  # pylint: disable=C0103

    # Extract, Transform Load - "application"
    df_raw = extract(DATASET)
    df_final = transform(df_raw)
    load(df_final, sql_repo, table_name)

    df_check = sql_repo.get(f"SELECT * FROM {table_name}")

    print(df_check.head(5))
    print(df_final.reset_index(drop=True).head(5))
