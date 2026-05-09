from fastapi import APIRouter, HTTPException
from typing import List
from ..models import maintenance_record as mr_models
from ..services import maintenance_service

router = APIRouter()

@router.post("/", response_model=mr_models.MaintenanceRecord)
def create_record(record_in: mr_models.MaintenanceRecordCreate):
    return maintenance_service.create_record(record_in)

# Additional endpoints (list, get) can be added similarly
