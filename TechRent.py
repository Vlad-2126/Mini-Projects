
from abc import ABC, abstractmethod
machine_dict = {}
customer_dict = {}

class Machine(ABC):
    def __init__(self,id,name,price_per_day):
        self.id = id
        self.name = name
        self._price_per_day = 0
        self.price_per_day = price_per_day
    
    @property
    def price_per_day(self):
        return self._price_per_day
    
    @price_per_day.setter
    def price_per_day(self,value):
        if value <= 0:
            raise ValueError("Price for rent cun`t be less than 0")
        self._price_per_day = value
    
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def __repr__(self):
        pass

class Excavator(Machine):
    def __init__(self, id, name, price_per_day, transport_speed, bucket_capacity):
        super().__init__(id, name, price_per_day)
        self.transport_speed = transport_speed
        self.bucket_capacity = bucket_capacity
    
    def __str__(self):
        return f"""Product id: {self.id}
    Product name: {self.name}
    Product rent price per day: {self.price_per_day}
    Product transporting speed: {self.transport_speed}
    Product bucket capacity: {self.bucket_capacity}"""
    
    def __repr__(self):
        return f"Name: {self.name}, id: {self.id}, price: {self.price_per_day}"

class Crane(Machine):
    def __init__(self, id, name, price_per_day, load_capacity, boom_reach):
        super().__init__(id, name, price_per_day)
        self.load_capacity = load_capacity
        self.boom_reach = boom_reach
        
    def __str__(self):
        return f"""Product id: {self.id}
    Product name: {self.name}
    Product rent price per day: {self.price_per_day}
    Product load capacity: {self.load_capacity}
    Product boom reach: {self.boom_reach}"""
    
    def __repr__(self):
        return f"Name: {self.name}, id: {self.id}, price: {self.price_per_day}"
        
class DrillRig(Machine):
    def __init__(self, id, name, price_per_day, drilling_depth, power):
        super().__init__(id, name, price_per_day)
        self.drilling_depth = drilling_depth
        self.power = power
        
    def __str__(self):
        return f"""Product id: {self.id}
    Product name: {self.name}
    Product rent price per day: {self.price_per_day}
    Product drilling depth: {self.drilling_depth}
    Product power: {self.power}"""
    
    def __repr__(self):
        return f"Name: {self.name}, id: {self.id}, price: {self.price_per_day}"
        
class MachineFactory(ABC):
    def register_machine(self,machine):
        machine_dict[machine.id] = machine
        
    def is_id_unique(self,id):
        if id in machine_dict.keys():
            raise InvalidProductNameError("Id must be unique")
    
    @abstractmethod
    def create_machine(self,*args):
        pass

class ExcavatorFactory(MachineFactory):
    def create_machine(self, id, name, price_per_day, transport_speed, bucket_capacity):
        excavator = Excavator(id, name, price_per_day, transport_speed, bucket_capacity)
        self.is_id_unique(id)
        self.register_machine(excavator)
        return excavator

class CraneFactory(MachineFactory):
    def create_machine(self, id, name, price_per_day, load_capacity, boom_reach):
        crane = Crane(id, name, price_per_day, load_capacity, boom_reach)
        self.is_id_unique(id)
        self.register_machine(crane)
        return crane
        
class DrillRigFactory(MachineFactory):
    def create_machine(self, id, name, price_per_day, drilling_depth, power):
        drill_rig = DrillRig(id, name, price_per_day, drilling_depth, power)
        self.is_id_unique(id)
        self.register_machine(drill_rig)
        return drill_rig

def create_product(factory : MachineFactory, *args, **kwargs):
    try:
        if not isinstance(factory,MachineFactory):
            raise InvalidProductNameError("Unknown type of product")
        transport = factory.create_machine(*args, **kwargs)
        return transport
    except ValueError as e:
        raise InvalidProductNameError(f"Error during product creation: {e}")

class Customer:
    def __init__(self, id, name, balance, rented_machines):
        self.id = id
        self.name = name
        self._balance = 0
        self.balance = balance
        self.rented_machines = rented_machines
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,value):
        if value >=0:
            self._balance = value

class InvalidProductNameError(Exception):
    pass


# create_product(ExcavatorFactory(),"id1000","Bob Cat Excavator", 1000, 10, 1)
# create_product(CraneFactory(),"id2000","Bob Cat Excavator", 1000, 10, 1)
# create_product(DrillRigFactory(),"id3000","Bob Cat Excavator", 1000, 10, 1)

