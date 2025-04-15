from .base import SimulatorBase
from datetime import datetime
import random

class PaymentSimulator(SimulatorBase):
    def __init__(self):
        super().__init__("payment.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": random.choices(["INFO", "ERROR"], weights=[85, 15])[0],
            "pid": random.randint(10000, 99999),
            "thread": f"nio-8080-exec-{random.randint(1, 10)}",
            "logger": "c.ecommerce.payment.PaymentService",
            "user_id": random.randint(1000, 2000),
            "amount": random.randint(1000, 50000)
        }
