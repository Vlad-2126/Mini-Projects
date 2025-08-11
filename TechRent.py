
from abc import ABC, abstractmethod
machin_dict = {}
customer_dict = {}

class Machine(ABC):
    def __init__(self,id,name,price_per_day):
        if id in machin_dict.keys():
            raise ValueError("Id must be unique")
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
    Product transporting spead: {self.transport_speed}
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
    @abstractmethod
    def create_machien(self,*args):
        return self

class ExcavatorFactory(MachineFactory):
    def create_machien(self, id, name, price_per_day, transport_spead, bucket_capacity):
        machin_dict[id] = Excavator(id, name, price_per_day, transport_spead, bucket_capacity)

class CraneFactory(MachineFactory):
    def create_machien(self, id, name, price_per_day, load_capacity, boom_reach):
        machin_dict[id] = Crane(id, name, price_per_day, load_capacity, boom_reach)
        
class DrillRigFactory(MachineFactory):
    def create_machien(self, id, name, price_per_day, drilling_depth, power):
        machin_dict[id] = DrillRig(id, name, price_per_day, drilling_depth, power)

def create_product(factory : MachineFactory, *args, **kwargs):
    if not isinstance(factory, MachineFactory):
        raise InvalidProductNameError("This product type is absent")
    transport = factory.create_machien(*args, **kwargs)
    print(machin_dict)
    return transport

class InvalidProductNameError(Exception):
    pass


create_product(NewcavatorFactory(),"id1000","Bob Cat Excavator", 1000, 10, 1)
create_product(CraneFactory(),"id2000","Bob Cat Excavator", 1000, 10, 1)
create_product(DrillRigFactory(),"id3000","Bob Cat Excavator", 1000, 10, 1)