from pydantic import BaseModel
from datetime import date

class RentalContractBase(BaseModel):
    machine_id: int
    user_id: int
    start_date: date
    end_date: date
    rent_amount: float
    terms: str | None = None

class RentalContractCreate(RentalContractBase):
    pass

class RentalContract(RentalContractBase):
    id: int
    class Config:
        orm_mode = True
