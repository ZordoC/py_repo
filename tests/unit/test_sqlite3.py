"""Unit test for SqliteRepository."""
import sqlite3

import pytest

from pd_repo.abstract_case.sql_repository import Sqlite3Repository
from pd_repo.scripts.abstract_example import get_random_string

DATABASE = "test_sqlite3.db"
TABLE = get_random_string(2)


@pytest.fixture
def conn():
    return sqlite3.connect(DATABASE)


def test_simple_connect(conn):
    assert conn.cursor()


def test_create_table(conn):
    conn.cursor().execute(f"CREATE TABLE {TABLE}(int_column, date_column)")
    res = conn.cursor().execute(f"""SELECT "name" FROM pragma_table_info("{TABLE}") LIMIT 1;""")
    result = res.fetchone()[0]
    assert result == "int_column"


def test_insert(conn):
    cur = conn.cursor()
    data = [
        (0, "10/11/10"),
        (1, "12/11/10"),
    ]
    cur.executemany(f"INSERT INTO {TABLE} VALUES(?, ?)", data)
    conn.commit()


def test_select(conn):
    cur = conn.cursor()
    res = cur.execute(f"SELECT * FROM {TABLE}")
    assert res.fetchall() == [(0, "10/11/10"), (1, "12/11/10")]


def test_get_columns(conn):
    cur = conn.cursor()
    pragmas = cur.execute(f"PRAGMA table_info({TABLE});")
    columns = [n for _, n, *_ in pragmas.fetchall()]

    assert columns == ["int_column", "date_column"]


@pytest.fixture()
def repo():
    return Sqlite3Repository(DATABASE)


def test_get(repo):
    df = repo.get(f"""SELECT * FROM {TABLE}""")
    assert not df.empty


def test_add(repo, test_df):
    repo.add(test_df, TABLE)


def test_drop_table(conn):
    conn.cursor().execute(f"DROP TABLE {TABLE}")
