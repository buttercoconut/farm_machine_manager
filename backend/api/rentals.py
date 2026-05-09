from fastapi import APIRouter, HTTPException
from typing import List
from ..models import rental_contract as rc_models
from ..services import rental_service

router = APIRouter()

@router.post("/", response_model=rc_models.RentalContract)
def create_contract(contract_in: rc_models.RentalContractCreate):
    return rental_service.create_contract(contract_in)

# Additional endpoints (list, get) can be added similarly
