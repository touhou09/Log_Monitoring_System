import random
from datetime import datetime
from simulator.base import SimulatorBase

class AuthSimulator(SimulatorBase):
    def __init__(self):
        super().__init__("auth.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": random.choices(["INFO", "ERROR"], weights=[80, 20])[0],
            "pid": random.randint(10000, 99999),
            "thread": f"nio-8080-exec-{random.randint(1, 10)}",
            "logger": "c.ecommerce.auth.AuthController",
            "user_id": random.randint(1000, 2000)
        }
