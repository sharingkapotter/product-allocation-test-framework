from src.db.db_client import AllocationDBClient
from utils.logger import get_logger

logger = get_logger("AllocationAPI")


class AllocationAPI:
    """
    Simulates an allocation service.
    """

    def __init__(self):
        self.db = AllocationDBClient()

    def allocate(self, payload: dict) -> dict:
        logger.info(f"Received allocation request: {payload}")

        demand = payload["demand"]
        capacity = payload["capacity"]

        allocated_quantity = min(demand, capacity)

        self.db.save_allocation(
            payload["store_id"],
            payload["product_id"],
            allocated_quantity
        )

        logger.info(
            f"Allocation completed: allocated_quantity={allocated_quantity}"
        )

        return {
            "store_id": payload["store_id"],
            "product_id": payload["product_id"],
            "allocated_quantity": allocated_quantity
        }
