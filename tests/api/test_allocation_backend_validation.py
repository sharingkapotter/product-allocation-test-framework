from src.api.allocation_api import AllocationAPI
from src.db.db_client import AllocationDBClient


def test_allocation_persisted_in_database():
    """
    Validates that allocation results are persisted in the backend DB.
    """

    api = AllocationAPI()
    db = AllocationDBClient()

    payload = {
        "store_id": 301,
        "product_id": 5001,
        "demand": 75,
        "capacity": 60
    }

    response = api.allocate(payload)

    db_value = db.get_allocation(
        payload["store_id"],
        payload["product_id"]
    )

    assert db_value == response["allocated_quantity"]
