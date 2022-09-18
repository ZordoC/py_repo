"""``Order`` module``"""
from dataclasses import dataclass


@dataclass
class Order:
    """Represents an order."""

    order_id: int
    sku: str
    qty: int
