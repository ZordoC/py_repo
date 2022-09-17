from pd_repo.domain_case.service_layer import SqlAlchemyRepository
from pd_repo.domain_case.domain import Order


def insert_order(session):
    session.execute(
        "INSERT INTO orders (order_id, sku, qty)" ' VALUES ("4", "CLEAN-PYTHON", 12)'
    )
    [[order_id]] = session.execute(
        "SELECT order_id FROM orders WHERE order_id=:order_id AND sku=:sku",
        dict(order_id="4", sku="CLEAN-PYTHON"),
    )
    return order_id


def get_order(session, order_id):
    order = session.query(Order).filter_by(order_id=order_id).one()
    return order


def test_can_retrieve_order(domain_session):

    order_id = insert_order(domain_session)

    repo = SqlAlchemyRepository(domain_session)

    order = repo.get(order_id)

    assert order_id == order.order_id


def test_can_load_order(domain_session):

    repo = SqlAlchemyRepository(domain_session)

    order = Order(129, "DESIGN-PATTERNS-PYTHON", 2)

    repo.add(order)

    order_from_db = get_order(domain_session, order.order_id)

    assert order == order_from_db

def test_can_list_orders(domain_session):

    repo = SqlAlchemyRepository(domain_session)

    orders = [
        Order(1, "CLEAN-CODE", 12),
        Order(2, "CLEAN-CODER", 13),
        Order(3, "CLEAN-ARCHITECTURE", 14),
    ]

    for order in orders:
        repo.add(order)


    orders_db = repo.list_order()

    assert orders == orders_db
