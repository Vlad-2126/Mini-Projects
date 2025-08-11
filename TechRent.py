machin_dict = {}
customer_dict = {}

class Machine:
    def __init__(self,id,name,price_per_day):
        self.id = id
        self.name = name
        self.price_per_day = price_per_day

class Excavator(Machine):
    def __init__(self, id, name, price_per_day, transport_spead, bucket_capacity):
        super().__init__(id, name, price_per_day)
        self.transport_spead = transport_spead
        self.bucket_capacity = bucket_capacity

class Crane(Machine):
    def __init__(self, id, name, price_per_day, load_capacity, boom_reach):
        super().__init__(id, name, price_per_day)
        self.load_capacity = load_capacity
        self.boom_reach = boom_reach
        
class DrillRig(Machine):
    def __init__(self, id, name, price_per_day, drilling_depth, power):
        super().__init__(id, name, price_per_day)
        self.drilling_depth = drilling_depth
        self.power = power