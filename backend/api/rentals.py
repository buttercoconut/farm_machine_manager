from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date

from ..database import get_db
from ..models.sql_models import RentalContract as RentalContractModel
from ..models.pydantic_models import RentalContract, RentalContractCreate

router = APIRouter()

@router.post("/", response_model=RentalContract, status_code=status.HTTP_201_CREATED)
def create_rental(contract: RentalContractCreate, db: Session = Depends(get_db)):
    # 비즈니스 로직: 같은 기계가 이미 대여 중인지 확인
    existing = db.query(RentalContractModel).filter(
        RentalContractModel.machine_id == contract.machine_id,
        RentalContractModel.end_date >= date.today()
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Machine is already rented during the requested period")
    db_contract = RentalContractModel(**contract.dict())
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

@router.get("/", response_model=list[RentalContract])
def read_rentals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contracts = db.query(RentalContractModel).offset(skip).limit(limit).all()
    return contracts

@router.get("/{contract_id}", response_model=RentalContract)
def read_rental(contract_id: int, db: Session = Depends(get_db)):
    contract = db.query(RentalContractModel).filter(RentalContractModel.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Rental contract not found")
    return contract

@router.put("/{contract_id}", response_model=RentalContract)
def update_rental(contract_id: int, contract: RentalContractCreate, db: Session = Depends(get_db)):
    db_contract = db.query(RentalContractModel).filter(RentalContractModel.id == contract_id).first()
    if not db_contract:
        raise HTTPException(status_code=404, detail="Rental contract not found")
    for key, value in contract.dict().items():
        setattr(db_contract, key, value)
    db.commit()
    db.refresh(db_contract)
    return db_contract

@router.delete("/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rental(contract_id: int, db: Session = Depends(get_db)):
    contract = db.query(RentalContractModel).filter(RentalContractModel.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Rental contract not found")
    db.delete(contract)
    db.commit()
    return None
