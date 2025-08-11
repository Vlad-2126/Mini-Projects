
from abc import ABC, abstractmethod
machin_dict = {}
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
            raise ValueError("Prise for rent cun`t be less than 0")
        self._price_per_day = value
    
    @abstractmethod
    def __str__(self):
        pass

class Excavator(Machine):
    def __init__(self, id, name, price_per_day, transport_spead, bucket_capacity):
        super().__init__(id, name, price_per_day)
        self.transport_spead = transport_spead
        self.bucket_capacity = bucket_capacity
    
    def __str__(self):
        return f"""Product id: {self.id}
    Product name: {self.name}
    Product rent price per day: {self.price_per_day}
    Product transporting spead: {self.transport_spead}
    Product bucket capacity: {self.bucket_capacity}"""

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
        
class MachineFactory(ABC):
    @abstractmethod
    def create_machin(self,*args):
        pass

class ExcavatorFactory(MachineFactory):
    def create_machin(self, id, name, price_per_day, transport_spead, bucket_capacity):
        machin_dict[id] = Excavator(id, name, price_per_day, transport_spead, bucket_capacity)

class CraneFactory(MachineFactory):
    def create_machin(self, id, name, price_per_day, load_capacity, boom_reach):
        machin_dict[id] = Crane(id, name, price_per_day, load_capacity, boom_reach)
        
class DrillRigFactory(MachineFactory):
    def create_machin(self, id, name, price_per_day, drilling_depth, power):
        machin_dict[id] = DrillRig(id, name, price_per_day, drilling_depth, power)

def create_product(factory : MachineFactory,):
    if factory not in machin_dict.values():
        raise InvalidProductNameError("This product type is absent")
    transport = factory.create_machin()
    print(machin_dict)
    return transport

class InvalidProductNameError(Exception):
    pass


create_product(ExcavatorFactory(1000,"Bob Cat Excavator", 1000, 10, 1))
# create_product(CraneFactory(1000,"Bob Cat Excavator", 1000, 10, 1))
# create_product(DrillRigFactory(1000,"Bob Cat Excavator", 1000, 10, 1))