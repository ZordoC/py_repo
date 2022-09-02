"""This is Python implementation of the Repository pattern, a simplifying
abstraction over data storage, allowing us to decouple our model layer from the
data layer."""

from abc import ABC, abstractmethod

import pandas as pd


class AbstractRepository(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
    """
    @abstractmethod
    def add(self, **kwargs) -> None:
        """_summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, **kwargs) -> pd.DataFrame:
        """_summary_

        Raises:
            NotImplementedError: _description_

        Returns:
            pd.DataFrame: _description_
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, **kwargs) -> None:
        """_summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
