import json
from src.api.allocation_api import AllocationAPI
from src.validators.allocation_validator import validate_allocation


def test_allocation_data_driven():
    """
    Data-driven test validating allocation logic
    across multiple products and stores.
    """

    api = AllocationAPI()

    with open("tests/data/allocation_test_data.json") as f:
        test_cases = json.load(f)

    for payload in test_cases:
        response = api.allocate(payload)

        validate_allocation(
            payload["demand"],
            payload["capacity"],
            response["allocated_quantity"]
        )
