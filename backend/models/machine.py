from pydantic import BaseModel, Field
from datetime import date

class MachineBase(BaseModel):
    model_name: str = Field(..., example="Tractor X200")
    manufacturer: str = Field(..., example="John Deere")
    purchase_date: date = Field(..., example="2022-05-15")
    serial_number: str = Field(..., example="SN123456789")
    description: str | None = None

class MachineCreate(MachineBase):
    pass

class Machine(MachineBase):
    id: int
    class Config:
        orm_mode = True
