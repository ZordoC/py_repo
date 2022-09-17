from pd_repo.domain_case.domain import Order


def test_orm_can_load_orders(domain_session):

    domain_session.execute(
        "INSERT INTO orders (order_id, sku, qty) VALUES "
        '(1, "CLEAN-CODE", 2),'
        '(2, "CLEAN-CODER", 2),'
        '(3, "CLEAN-ARCHITECTURE", 3)'
    )

    expected = [
        Order(1, "CLEAN-CODE", 12),
        Order(2, "CLEAN-CODER", 13),
        Order(3, "CLEAN-ARCHITECTURE", 14),
    ]

    domain_session.query(Order).all() == expected


def test_orm_can_save_order(domain_session):

    orders = [
        Order(1, "CLEAN-CODE", 12),
        Order(2, "CLEAN-CODER", 13),
        Order(3, "CLEAN-ARCHITECTURE", 14),
    ]

    for order in orders:
        domain_session.add(order)

    domain_session.commit()

    rows = list(domain_session.execute('SELECT * FROM "orders"'))

    assert rows == [
        ((1, "CLEAN-CODE", 12)),
        (2, "CLEAN-CODER", 13),
        (3, "CLEAN-ARCHITECTURE", 14),
    ]
