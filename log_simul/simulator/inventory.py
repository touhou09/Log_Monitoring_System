from faker import Faker
from datetime import datetime
from simulator.base import SimulatorBase

fake = Faker()

class InventorySimulator(SimulatorBase):
    def __init__(self):
        super().__init__("inventory.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": fake.random_element(["INFO"] * 19 + ["WARN"]),
            "pid": fake.random_int(10000, 99999),
            "thread": f"nio-8080-exec-{fake.random_int(1, 10)}",
            "logger": "c.ecommerce.inventory.InventoryClient",
            "item_id": f"ITEM-{fake.bothify(text='???###')}",
            "remaining": fake.random_int(0, 5)
        }
