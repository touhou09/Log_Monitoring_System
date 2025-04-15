from .base import SimulatorBase
from datetime import datetime
import random
from datetime import datetime
from simulator.base import SimulatorBase

class OrderSimulator(SimulatorBase):
    def __init__(self):
        super().__init__("order.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": random.choices(["INFO", "ERROR"], weights=[90, 10])[0],
            "pid": random.randint(10000, 99999),
            "thread": f"nio-8080-exec-{random.randint(1, 10)}",
            "logger": "c.ecommerce.order.OrderService",
            "user_id": random.randint(1000, 2000),
            "product_id": random.randint(2000, 3000)
        }