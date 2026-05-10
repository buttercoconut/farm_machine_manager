from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.sql_models import MaintenanceRecord as MaintenanceRecordModel
from ..models.pydantic_models import MaintenanceRecord, MaintenanceRecordCreate

router = APIRouter()

@router.post("/", response_model=MaintenanceRecord, status_code=status.HTTP_201_CREATED)
def create_maintenance(record: MaintenanceRecordCreate, db: Session = Depends(get_db)):
    db_record = MaintenanceRecordModel(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/", response_model=list[MaintenanceRecord])
def read_maintenances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = db.query(MaintenanceRecordModel).offset(skip).limit(limit).all()
    return records

@router.get("/{record_id}", response_model=MaintenanceRecord)
def read_maintenance(record_id: int, db: Session = Depends(get_db)):
    record = db.query(MaintenanceRecordModel).filter(MaintenanceRecordModel.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    return record

@router.put("/{record_id}", response_model=MaintenanceRecord)
def update_maintenance(record_id: int, record: MaintenanceRecordCreate, db: Session = Depends(get_db)):
    db_record = db.query(MaintenanceRecordModel).filter(MaintenanceRecordModel.id == record_id).first()
    if not db_record:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    for key, value in record.dict().items():
        setattr(db_record, key, value)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenance(record_id: int, db: Session = Depends(get_db)):
    record = db.query(MaintenanceRecordModel).filter(MaintenanceRecordModel.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    db.delete(record)
    db.commit()
    return None
