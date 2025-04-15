import random
from datetime import datetime
from simulator.base import SimulatorBase

class NotifySimulator(SimulatorBase):
    def __init__(self):
        super().__init__("notify.j2")

    def generate_log(self, now: datetime) -> dict:
        return {
            "timestamp": now,
            "level": random.choices(["INFO", "ERROR"], weights=[95, 5])[0],
            "pid": random.randint(10000, 99999),
            "thread": f"nio-8080-exec-{random.randint(1, 10)}",
            "logger": "c.ecommerce.notify.NotifyService",
            "user_id": random.randint(1000, 2000),
            "notif_type": random.choice(["SMS", "EMAIL", "PUSH"])
        }
