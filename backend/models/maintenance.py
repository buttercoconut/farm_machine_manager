from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class MaintenanceRecord(Base):
    __tablename__ = "maintenance_records"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    maintenance_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

    machine = relationship("Machine", back_populates="maintenance_records")
