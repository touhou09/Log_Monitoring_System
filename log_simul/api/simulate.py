from fastapi import APIRouter
from simulator.order import OrderSimulator
from simulator.payment import PaymentSimulator
from simulator.inventory import InventorySimulator
from simulator.notify import NotifySimulator
from simulator.auth import AuthSimulator
from simulator.etc import EtcSimulator
from datetime import datetime
from stream_queue import publish_to_streams

router = APIRouter()

simulators = {
    "order": OrderSimulator(),
    "payment": PaymentSimulator(),
    "inventory": InventorySimulator(),
    "notify": NotifySimulator(),
    "auth": AuthSimulator(),
    "etc": EtcSimulator()
}

@router.get("/simulate/{service}")
async def simulate(service: str):
    now = datetime.utcnow()
    simulator = simulators.get(service)
    if not simulator:
        return {"error": "invalid service"}
    log = simulator.generate_log(now)
    rendered = simulator.render(log)
    await publish_to_streams(service, rendered)
    return {"queued": log}
