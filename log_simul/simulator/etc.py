import random
from datetime import datetime
from simulator.base import SimulatorBase

class EtcSimulator(SimulatorBase):
    def __init__(self):
        super().__init__("etc.j2")

    def generate_log(self, now: datetime) -> dict:
        domain = random.choice(["product", "review", "coupon"])
        return {
            "timestamp": now,
            "level": random.choices(["INFO", "ERROR"], weights=[90, 10])[0],
            "pid": random.randint(10000, 99999),
            "thread": f"nio-8080-exec-{random.randint(1, 10)}",
            "logger": f"c.ecommerce.{domain}.{domain.title()}Service",
            "domain": domain
        }
