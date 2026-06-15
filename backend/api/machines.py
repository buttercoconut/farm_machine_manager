from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/machines", tags=["machines"])

@router.post("/", response_model=schemas.Machine)
async def create_machine(machine: schemas.MachineCreate, db: Session = Depends(get_db)):
    db_machine = models.Machine(**machine.dict())
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine

@router.get("/", response_model=list[schemas.Machine])
async def list_machines(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    machines = db.query(models.Machine).offset(skip).limit(limit).all()
    return machines
