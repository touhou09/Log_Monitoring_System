from faker import Faker
from datetime import datetime
from simulator.base import SimulatorBase

fake = Faker()

class EtcSimulator(SimulatorBase):
    def __init__(self):
        super().__init__("etc.j2")

    def generate_log(self, now: datetime) -> dict:
        domain = fake.random_element(["product", "review", "coupon"])
        return {
            "timestamp": now,
            "level": fake.random_element(["INFO"] * 9 + ["ERROR"]),
            "pid": fake.random_int(10000, 99999),
            "thread": f"nio-8080-exec-{fake.random_int(1, 10)}",
            "logger": f"c.ecommerce.{domain}.{domain.title()}Service",
            "domain": domain
        }
