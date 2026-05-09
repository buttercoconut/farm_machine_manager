from pydantic import BaseModel, Field
from datetime import date

class RentalContractBase(BaseModel):
    machine_id: int
    renter_id: int
    start_date: date
    end_date: date
    rental_fee: float
    terms: str | None = None

class RentalContractCreate(RentalContractBase):
    pass

class RentalContract(RentalContractBase):
    id: int
    class Config:
        orm_mode = True
