from pydantic import BaseModel
from datetime import date

class MaintenanceRecordBase(BaseModel):
    machine_id: int
    maintenance_date: date
    description: str
    cost: float

class MaintenanceRecordCreate(MaintenanceRecordBase):
    pass

class MaintenanceRecord(MaintenanceRecordBase):
    id: int
    class Config:
        orm_mode = True
