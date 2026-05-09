# Service layer placeholder for machine operations
from typing import List
from . import machine as machine_models

# In-memory store for demo purposes
_machines: List[machine_models.Machine] = []

def create_machine(machine_in: machine_models.MachineCreate) -> machine_models.Machine:
    new_id = len(_machines) + 1
    machine = machine_models.Machine(id=new_id, **machine_in.dict())
    _machines.append(machine)
    return machine

def get_machine(machine_id: int) -> machine_models.Machine | None:
    return next((m for m in _machines if m.id == machine_id), None)

def list_machines() -> List[machine_models.Machine]:
    return _machines
