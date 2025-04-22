from faker import Faker
from datetime import datetime
from simulator.base import SimulatorBase

fake = Faker()

class OrderSimulator(SimulatorBase):
    def __init__(self):
        super().__init__("order.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": fake.random_element(["INFO"] * 9 + ["ERROR"]),
            "pid": fake.random_int(10000, 99999),
            "thread": f"nio-8080-exec-{fake.random_int(1, 10)}",
            "logger": "c.ecommerce.order.OrderService",
            "user_id": fake.uuid4(),
            "product_id": fake.random_int(10000, 99999)
        }
