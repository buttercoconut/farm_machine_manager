from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..models import machine as machine_models
from ..services import machine_service

router = APIRouter()

@router.post("/", response_model=machine_models.Machine)
def create_machine(machine_in: machine_models.MachineCreate):
    return machine_service.create_machine(machine_in)

@router.get("/", response_model=List[machine_models.Machine])
def list_machines():
    return machine_service.list_machines()

@router.get("/{machine_id}", response_model=machine_models.Machine)
def read_machine(machine_id: int):
    machine = machine_service.get_machine(machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine
