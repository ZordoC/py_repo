"""Tests for MongoRepository using FakeRepository"""
import pandas as pd
import pytest

from pd_repo.nosql_repository import FakeNoSqlRepository


@pytest.fixture()
def repo():
    return FakeNoSqlRepository()

def test_insert(repo):
    """Simplet test for insert_one method"""
    repo.insert_one({"name": "jose", "age": 26}, "collection_1")
    assert repo._db["collection_1"][0] == {"name": "jose", "age": 26}


def test_list_all(repo):
    """Simple test for list all method"""
    repo._db['collection_1'].append({"name": "jose", "age": 26})
    res = repo.list_all("collection_1")
    assert res == [{"name": "jose", "age": 26}]
    repo._db['collection_1'].append({"name": "anna", "age": 27})
    assert res == [{"name": "jose", "age": 26}, {"name": "anna", "age": 27}]
