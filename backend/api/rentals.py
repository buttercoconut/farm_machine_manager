from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/rentals", tags=["rentals"])

@router.post("/", response_model=schemas.RentalContract)
async def create_rental_contract(contract: schemas.RentalContractCreate, db: Session = Depends(get_db)):
    # Basic validation: check machine exists
    machine = db.query(models.Machine).filter(models.Machine.id == contract.machine_id).first()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    # Check user exists
    user = db.query(models.User).filter(models.User.id == contract.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db_contract = models.RentalContract(**contract.dict())
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract
