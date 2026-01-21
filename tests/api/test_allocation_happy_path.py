from src.api.allocation_api import AllocationAPI
from src.validators.allocation_validator import validate_allocation


def test_allocation_happy_path():
    """
    Happy path test:
    Demand is less than capacity.
    """

    api = AllocationAPI()

    payload = {
        "store_id": 101,
        "product_id": 555,
        "demand": 80,
        "capacity": 100
    }

    response = api.allocate(payload)

    validate_allocation(
        payload["demand"],
        payload["capacity"],
        response["allocated_quantity"]
    )
