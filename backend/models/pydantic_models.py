from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class MachineBase(BaseModel):
    model_name: str
    manufacturer: str
    purchase_date: date
    serial_number: str

class MachineCreate(MachineBase):
    pass

class Machine(MachineBase):
    id: int
    serial_number: str

    class Config:
        orm_mode = True

class MaintenanceRecordBase(BaseModel):
    maintenance_date: date
    description: str
    cost: float

class MaintenanceRecordCreate(MaintenanceRecordBase):
    pass

class MaintenanceRecord(MaintenanceRecordBase):
    id: int
    machine_id: int

    class Config:
        orm_mode = True

class RentalContractBase(BaseModel):
    renter_name: str
    start_date: date
    end_date: date
    rental_fee: float
    terms: Optional[str] = None

class RentalContractCreate(RentalContractBase):
    machine_id: int

class RentalContract(RentalContractBase):
    id: int
    machine_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True
