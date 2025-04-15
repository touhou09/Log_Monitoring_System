from simulator.order import OrderSimulator
from simulator.payment import PaymentSimulator
from simulator.inventory import InventorySimulator
from simulator.notify import NotifySimulator
from simulator.auth import AuthSimulator
from simulator.etc import EtcSimulator

def get_all_simulators():
    return {
        "order": OrderSimulator(),
        "payment": PaymentSimulator(),
        "inventory": InventorySimulator(),
        "notify": NotifySimulator(),
        "auth": AuthSimulator(),
        "etc": EtcSimulator(),
    }
