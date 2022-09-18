"""Module for FakeRepository."""
from typing import List

from pd_repo.domain_case.domain import Order

from ._base import AbstractOrderRepository

FAKE_ORDERS = [
    Order(1, "CLEAN-CODE", 12),
    Order(2, "CLEAN-CODER", 13),
    Order(3, "CLEAN-ARCHITECTURE", 14),
]


class FakeOrderRepository(AbstractOrderRepository):
    """Fake implementation used for testing."""

    def __init__(self, orders: List[Order]):
        self._orders = list(orders)

    def add(self, order: Order):
        """Add an ``Order`` object to our persistant storage.

        Args:
            order (Order): An object representing an order.
        """
        self._orders.append(order)

    def get(self, order_id: int):
        """Get an order from our persistant storage.

        Args:
            order_id (int): Id of order.

        Returns:
            Order: ``Order`` matching with ``order_id``.
        """
        return next(b for b in self._orders if b.order_id == order_id)

    def list_order(self):
        """List all ``Orders``.

        Returns:
            list: List containing all orders in ``Order`` format.
        """
        return list(self._orders)
