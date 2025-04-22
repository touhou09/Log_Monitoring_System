from faker import Faker
from datetime import datetime
from simulator.base import SimulatorBase

fake = Faker()

class AuthSimulator(SimulatorBase):
    def __init__(self):
        super().__init__("auth.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": fake.random_element(["INFO"] * 8 + ["ERROR"] * 2),
            "pid": fake.random_int(10000, 99999),
            "thread": f"nio-8080-exec-{fake.random_int(1, 10)}",
            "logger": "c.ecommerce.auth.AuthController",
            "user_id": fake.uuid4()
        }
