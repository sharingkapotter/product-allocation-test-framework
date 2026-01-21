import sqlite3
from config.config import DB_NAME
from utils.logger import get_logger

logger = get_logger("DBClient")


class AllocationDBClient:
    def __init__(self):
        self.db_path = DB_NAME
        self._initialize_db()

    def _initialize_db(self):
        logger.info("Initializing allocation database")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS allocations (
                store_id INTEGER,
                product_id INTEGER,
                allocated_quantity INTEGER
            )
        """)

        conn.commit()
        conn.close()

    def save_allocation(self, store_id, product_id, allocated_quantity):
        logger.info(
            f"Saving allocation: store={store_id}, product={product_id}, qty={allocated_quantity}"
        )

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO allocations VALUES (?, ?, ?)",
            (store_id, product_id, allocated_quantity)
        )

        conn.commit()
        conn.close()

    def get_allocation(self, store_id, product_id):
        logger.info(
            f"Fetching allocation: store={store_id}, product={product_id}"
        )

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT allocated_quantity FROM allocations WHERE store_id=? AND product_id=?",
            (store_id, product_id)
        )

        result = cursor.fetchone()
        conn.close()

        return result[0] if result else None
