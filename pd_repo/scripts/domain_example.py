"""Example script for domain case using ``Orders`` and ORM."""
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pd_repo.domain_case.domain import Order
from pd_repo.domain_case.service_layer import (
    AbstractOrderRepository,
    SqlAlchemyOrderRepository,
    metadata,
    start_mappers,
)


def start_in_memory_db():
    """Start a in-memory DB using sqlalchemy."""
    Session = sessionmaker()  # pylint: disable=C0103
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    start_mappers()
    Session.configure(bind=engine)
    session = Session()
    return session


def extract() -> List[Order]:
    """Dummy method to represent getting data from somwehere.

    Returns:
        List: List containing Orders.
    """
    orders = [
        Order(10, "CLEAN-CODE", 8),
        Order(11, "CLEAN-CODER", 3),
        Order(12, "CLEAN-ARCHITECTURE", 1),
    ]
    return orders


def transform(orders: List[Order], qty: int = 10) -> List[Order]:
    """Increments qty on each ``Order``

    Args:
        orders (List[Order]): A List of Orders.

    Returns:
        List[Order]: List of Orders with  extra qty.
    """
    for order in orders:
        order.qty += qty
    return orders


def load(orders: List[Order], repo: AbstractOrderRepository):
    """Load transformed data into a Database.

    Args:
        repo (AbstractOrdersRepository): _description_
        orders (List[Order]): _description_
    """
    for order in orders:
        repo.add(order)


def etl(repo: AbstractOrderRepository):
    """Runs extract, transform and load pipelines.

    Args:
        repo (AbstractOrderRepository): Repository with connection to a database.
    """
    orders = extract()

    orders_transformed = transform(orders)

    load(orders_transformed, repo)


if __name__ == "__main__":

    session_ = start_in_memory_db()
    order_repo = SqlAlchemyOrderRepository(session_)

    etl(order_repo)

    print(order_repo.list_order())
