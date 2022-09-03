"""Unit test for SqliteRepository."""
import sqlite3

import pandas as pd
import pytest

DATABASE = "test_sqlite3.db"
TABLE = "test_table"


@pytest.fixture
def conn():
    return sqlite3.connect(DATABASE)


def test_simple_connect(conn):
    assert conn.cursor()


def test_create_table(conn):
    conn.cursor().execute(f"CREATE TABLE {TABLE}(int_column, date_column)")
    res = conn.cursor().execute(
        f"""SELECT "name" FROM pragma_table_info("{TABLE}") LIMIT 1;"""
    )
    result = res.fetchone()[0]
    print(result)
    assert result == 'int_column'

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
    assert res.fetchall() == [(0, '10/11/10'), (1, '12/11/10')]


def test_drop_table(conn):
    conn.cursor().execute(f"DROP TABLE {TABLE}")


# data=[[0, "10/11/12"], [1, "12/11/10"]], columns=["int_column", "date_column"]
