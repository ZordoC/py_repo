"""Module containing a ``AbstractOrdersRepository`` implementation using
sqlalchemy."""
from sqlalchemy.orm.session import Session

from pd_repo.domain_case.domain import Order

from ._base import AbstractOrdersRepository


class SqlAlchemyOrderRepository(AbstractOrdersRepository):
    """Implementation of the ``AbstractOrderRepository`` using sqlalchemy
    library."""

    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order):
        """Add an ``Order`` object to our persistant storage.

        Args:
            order (Order): An object representing an order.
        """
        self.session.add(order)

    def get(self, order_id: int):
        """Get an order from our persistant storage.

        Args:
            order_id (int): Id of order.

        Returns:
            Order: ``Order`` matching with ``order_id``.
        """
        return self.session.query(Order).filter_by(order_id=order_id).one()

    def list_order(self) -> list:
        """List all ``Orders``.

        Returns:
            list: List containing all orders in ``Order`` format.
        """
        return self.session.query(Order).all()
