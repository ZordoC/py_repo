"""Module containing custom exceptions for SqliteRepository."""


class SqliteRepositoryError(Exception):
    """Raised when ``SqliteRepository`` errors occur."""


class NotADeleteQuery(Exception):
    """Raised when using delete method without a DELETE statement."""
