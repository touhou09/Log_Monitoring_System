import random
from datetime import datetime
from simulator.base import SimulatorBase

class InventorySimulator(SimulatorBase):
    def __init__(self):
        super().__init__("inventory.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": random.choices(["INFO", "WARN"], weights=[95, 5])[0],
            "pid": random.randint(10000, 99999),
            "thread": f"nio-8080-exec-{random.randint(1, 10)}",
            "logger": "c.ecommerce.inventory.InventoryClient",
            "item_id": f"ITEM{random.randint(100, 999)}",
            "remaining": random.randint(0, 5)
        }
