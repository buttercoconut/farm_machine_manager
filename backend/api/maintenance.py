from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/maintenance", tags=["maintenance"])

@router.post("/", response_model=schemas.MaintenanceRecord)
async def create_maintenance(record: schemas.MaintenanceRecordCreate, db: Session = Depends(get_db)):
    machine = db.query(models.Machine).filter(models.Machine.id == record.machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    db_record = models.MaintenanceRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
