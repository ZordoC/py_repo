import abc

from pd_repo.domain_case.domain import Order


class AbstractRepository(abc.ABC):
    @abc.abstractmethod  # (1)
    def add(self, order: Order):
        raise NotImplementedError  # (2)

    @abc.abstractmethod
    def get(self, reference) -> Order:
        raise NotImplementedError
