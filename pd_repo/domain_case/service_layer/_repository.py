from sqlalchemy.orm.session import Session

from pd_repo.domain_case.domain import Order

from ._base import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order):
        self.session.add(order)

    def get(self, order_id: int):
        return self.session.query(Order).filter_by(order_id=order_id).one()

    def list_order(self):
        return self.session.query(Order).all()
