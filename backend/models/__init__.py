from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    purchase_date = Column(Date, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)
    description = Column(String)

    maintenance_records = relationship("MaintenanceRecord", back_populates="machine")
    rental_contracts = relationship("RentalContract", back_populates="machine")

class MaintenanceRecord(Base):
    __tablename__ = "maintenance_records"
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    maintenance_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

    machine = relationship("Machine", back_populates="maintenance_records")

class RentalContract(Base):
    __tablename__ = "rental_contracts"
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    rent_amount = Column(Float, nullable=False)
    terms = Column(String)

    machine = relationship("Machine", back_populates="rental_contracts")
    user = relationship("User", back_populates="rental_contracts")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String)
    hashed_password = Column(String, nullable=False)

    rental_contracts = relationship("RentalContract", back_populates="user")
