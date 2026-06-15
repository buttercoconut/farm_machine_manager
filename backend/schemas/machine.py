from pydantic import BaseModel
from datetime import date

class MachineBase(BaseModel):
    model_name: str
    manufacturer: str
    purchase_date: date
    serial_number: str
    description: str | None = None

class MachineCreate(MachineBase):
    pass

class Machine(MachineBase):
    id: int
    class Config:
        orm_mode = True
