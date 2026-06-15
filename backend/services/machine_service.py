from sqlalchemy.orm import Session
from ..models.machine import MachineCreate, Machine, MachineUpdate
from ..models.rental_contract import RentalContractCreate, RentalContract, RentalContractUpdate
from ..models.machine import Machine as MachineModel
from ..models.rental_contract import RentalContract as RentalContractModel

class MachineService:
    def __init__(self, db: Session):
        self.db = db

    def create_machine(self, machine_in: MachineCreate) -> Machine:
        machine = MachineModel(**machine_in.dict())
        self.db.add(machine)
        self.db.commit()
        self.db.refresh(machine)
        return machine

    def get_all_machines(self):
        return self.db.query(MachineModel).all()

    def get_machine(self, machine_id: int):
        return self.db.query(MachineModel).filter(MachineModel.id == machine_id).first()

    def update_machine(self, machine_id: int, machine_in: MachineUpdate):
        machine = self.get_machine(machine_id)
        if not machine:
            return None
        for var, value in machine_in.dict(exclude_unset=True).items():
            setattr(machine, var, value)
        self.db.commit()
        self.db.refresh(machine)
        return machine

    def delete_machine(self, machine_id: int) -> bool:
        machine = self.get_machine(machine_id)
        if not machine:
            return False
        self.db.delete(machine)
        self.db.commit()
        return True

class RentalService:
    def __init__(self, db: Session):
        self.db = db

    def create_contract(self, contract_in: RentalContractCreate) -> RentalContract:
        contract = RentalContractModel(**contract_in.dict())
        self.db.add(contract)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def get_all_contracts(self):
        return self.db.query(RentalContractModel).all()

    def get_contract(self, contract_id: int):
        return self.db.query(RentalContractModel).filter(RentalContractModel.id == contract_id).first()

    def update_contract(self, contract_id: int, contract_in: RentalContractUpdate):
        contract = self.get_contract(contract_id)
        if not contract:
            return None
        for var, value in contract_in.dict(exclude_unset=True).items():
            setattr(contract, var, value)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def delete_contract(self, contract_id: int) -> bool:
        contract = self.get_contract(contract_id)
        if not contract:
            return False
        self.db.delete(contract)
        self.db.commit()
        return True
