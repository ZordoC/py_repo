"""This is Python implementation of the Repository pattern, a simplifying
abstraction over data storage, allowing us to decouple our model layer from the
data layer."""

from abc import ABC, abstractmethod

import pandas as pd


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, **kwargs) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def delete(self, **kwargs) -> None:
        raise NotImplementedError
