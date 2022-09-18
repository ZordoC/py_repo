"""Testing for domain example."""
from pd_repo.domain_case.service_layer import FAKE_ORDERS, FakeOrderRepository
from pd_repo.scripts.domain_example import etl


def test_order_etl():
    repo = FakeOrderRepository(
        FAKE_ORDERS
    )  # No need to create session, we can easily validate results

    etl(repo)

    assert len(repo.list_order()) > len(FAKE_ORDERS)
    assert repo.list_order()[0] == FAKE_ORDERS[0]
    assert repo.list_order()[1] == FAKE_ORDERS[1]
    assert repo.list_order()[2] == FAKE_ORDERS[2]
    assert repo.list_order()[3] not in FAKE_ORDERS
