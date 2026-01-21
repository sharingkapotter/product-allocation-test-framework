from src.api.allocation_api import AllocationAPI
from src.validators.allocation_validator import validate_allocation


def test_allocation_when_demand_exceeds_capacity():
    """
    Demand is higher than capacity.
    Allocation should be capped at capacity.
    """
    api = AllocationAPI()

    payload = {
        "store_id": 101,
        "product_id": 999,
        "demand": 200,
        "capacity": 100
    }

    response = api.allocate(payload)

    assert response["allocated_quantity"] == payload["capacity"]
    validate_allocation(
        payload["demand"],
        payload["capacity"],
        response["allocated_quantity"]
    )


def test_allocation_when_demand_is_zero():
    """
    Zero demand should result in zero allocation.
    """
    api = AllocationAPI()

    payload = {
        "store_id": 102,
        "product_id": 888,
        "demand": 0,
        "capacity": 50
    }

    response = api.allocate(payload)

    assert response["allocated_quantity"] == 0
