"""Module responsible for the ORM mapping of Order objects and orders table."""
from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper

from pd_repo.domain_case.domain import Order

metadata = MetaData()

order = Table(
    "orders",
    metadata,
    Column("order_id", Integer, primary_key=True),
    Column("sku", String(255), nullable=False),
    Column("qty", Integer, nullable=False),
)


def start_mappers():
    """Map ``Order`` to orders table."""
    mapper(Order, order)
