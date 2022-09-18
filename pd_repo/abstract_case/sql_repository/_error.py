"""Module containing custom exceptions for SqliteRepository."""


class SqliteRepositoryError(Exception):
    """Raised when ``SqliteRepository`` errors occur."""


class NotADeleteQuery(Exception):
    """Raised when using delete method without a DELETE statement."""


class TableDoesNotExistError(Exception):
    """Raise when ``FakeRepository`` is passed a table that it's not defined in
    its constructor."""
