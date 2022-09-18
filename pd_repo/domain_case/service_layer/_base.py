"""Abstract class for repository type classes."""
import abc

from pd_repo.domain_case.domain import Order


class AbstractOrderRepository(abc.ABC):
    """Defines an interface for repository family type classes."""

    @abc.abstractmethod
    def add(self, order: Order):
        """Add an ``Order`` object to our persistant storage.

        Args:
            order (Order): An object representing an order.

        Raises:
            NotImplementedError: Abstract classes have no implementation
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, order_id: int) -> Order:
        """Get an order from our persistant storage.

        Args:
            order_id (int): Id of order.

        Returns:
            Order: ``Order`` matching with ``order_id``.

        Raises:
            NotImplementedError: Abstract classes have no implementation
        """
        raise NotImplementedError

    @abc.abstractmethod
    def list_order(self) -> list:
        """List all ``Orders``.

        Returns:
            list: List containing all orders in ``Order`` format.

        Raises:
                NotImplementedError: Abstract classes have no implementation
        """
        raise NotImplementedError
