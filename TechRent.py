
from abc import ABC, abstractmethod
from datetime import datetime
from random import randint
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
        self.is_id_unique(id)
        excavator = Excavator(id, name, price_per_day, transport_speed, bucket_capacity)
        self.register_machine(excavator)
        return excavator

class CraneFactory(MachineFactory):
    def create_machine(self, id, name, price_per_day, load_capacity, boom_reach):
        self.is_id_unique(id)
        crane = Crane(id, name, price_per_day, load_capacity, boom_reach)
        self.register_machine(crane)
        return crane
        
class DrillRigFactory(MachineFactory):
    def create_machine(self, id, name, price_per_day, drilling_depth, power):
        self.is_id_unique(id)
        drill_rig = DrillRig(id, name, price_per_day, drilling_depth, power)
        self.register_machine(drill_rig)
        return drill_rig
class ProductManager:
    @staticmethod
    def create_product(factory : MachineFactory, *args, **kwargs):
        try:
            if not isinstance(factory,MachineFactory):
                raise InvalidMachineTypeError("Unknown type of product")
            transport = factory.create_machine(*args, **kwargs)
            return transport
        except ValueError as e:
            raise InvalidProductNameError(f"Error during product creation: {e}")
    
    @staticmethod
    def get_renting_customer(machine_id):
        for customer in customer_dict.values():
            if machine_id in customer.rented_machines:
                return customer
        return None
    
    @staticmethod
    def machine_rent(customer_id,machine_id,days):
        if customer_id not in customer_dict:
            raise ClientNotFoundError("Current user does not exist")
        if ProductManager.get_renting_customer(machine_id):
            raise MachineAlreadyRentedError("This machine is currently rented and can not be rented again")
        customer = customer_dict[customer_id]
        customer.rent_machine(machine_id,days)
    
    @staticmethod
    def return_rent(machine_id):
        renting_customer = ProductManager.get_renting_customer(machine_id)
        if not renting_customer:
            raise InvalidProductDataError("This machine is not rented and can not be returned")
        else:
            renting_customer.rented_machines.remove(machine_id)
    

class Customer:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self._balance = 0
        self.balance = balance
        self.rented_machines = []
    
    def __str__(self):
        return f"""Customer's info
    id: {self.id}
    name: {self.name}
    balance: {self.balance}
    rented machines: {self.rented_machines}"""
    
    def __repr__(self):
        return f"id:{self.id}, name: {self.name}, balance: {self.balance}, rented machines: {self.rented_machines}"
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Balance can not be negative")
        self._balance = value
    
    def top_up_balance(self, amount):
        self_id = self.id
        payment_method = "card"
        if amount <= 0:
            raise ValueError("Amount can not be negative")
        self._balance += amount
        transaction = DepositTransactionFactory.create_transacrion(amount, self_id, payment_method)
        TransactionFactory.add_transaction(transaction)
        print(f"Your balance was successfully topped up by {amount}$")
    
    def rent_machine(self,machine_id,days):
        self_id = self.id
        if machine_id in machine_dict.keys():
            if days<=0:
                raise ValueError("You can not rent machine for less than one day")
            daily_rate = machine_dict[machine_id].price_per_day
            final_price = days*daily_rate
            if final_price <= self._balance:
                self.balance -= final_price
                self.rented_machines.append(machine_id)
                transaction = RentalTransactionFactory.create_transacrion(-final_price, days, self_id, machine_id, daily_rate)
                TransactionFactory.add_transaction(transaction)
                print(f"Machine {machine_dict[machine_id].name} was successfully rented for {days} days.")
            else:
                raise ValueError("Not enough money on your balance") 
        else:
            raise ValueError("Current machine does not exist")

class PhysicalPerson(Customer):
    def __init__(self, id, name, balance, passport_number, age):
        super().__init__(id, name, balance)
        self.passport_number = passport_number
        self._age = 0
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if int(value) < 18:
            raise ValueError("Minors can not be physical person")
        self._age = value
    
    def __str__(self):
        return f"""Customer's info
    id: {self.id}
    name: {self.name}
    balance: {self.balance}
    rented machines: {self.rented_machines}
    passport number: {self.passport_number}
    age: {self.age}"""
    
    def __repr__(self):
        return f"id:{self.id}, name: {self.name}, balance: {self.balance}, rented machines: {self.rented_machines}, passport number: {self.passport_number}, age: {self.age}"
    

class LegalEntity(Customer):
    def __init__(self, id, name, balance, registration_number, tax_id):
        super().__init__(id, name, balance)
        self.registration_number = registration_number
        self.tax_id = tax_id
    
    def __str__(self):
        return f"""Customer's info
    id: {self.id}
    name: {self.name}
    balance: {self.balance}
    rented machines: {self.rented_machines}
    registration number: {self.registration_number}
    tax id: {self.tax_id}
    """
    
    def __repr__(self):
        return f"id:{self.id}, name: {self.name}, balance: {self.balance}, rented machines: {self.rented_machines}, registration number: {self.registration_number}, tax id: {self.tax_id}"
    
class Company(Customer):
    def __init__(self, id, name, balance, industry, employee_count):
        super().__init__(id, name, balance)
        self.industry = industry   
        self.employee_count = employee_count
    
    def __str__(self):
        return f"""Customer's info
    id: {self.id}
    name: {self.name}
    balance: {self.balance}
    rented machines: {self.rented_machines}
    industry: {self.industry}
    employee count: {self.employee_count}
    """
    
    def __repr__(self):
        return f"id:{self.id}, name: {self.name}, balance: {self.balance}, rented machines: {self.rented_machines}, industry: {self.industry}, employee count: {self.employee_count}"
    

class CustomerFactory(ABC):
    def add_customer(self,customer):
        customer_dict[customer.id] = customer
    
    def is_id_unique(self,id):
        if id in customer_dict.keys():
            raise InvalidCustomerDataError("Customer id must be unique")
    
    @abstractmethod
    def create_customer(self,*args):
        pass

class PhysicalPersonFactory(CustomerFactory):
    def create_customer(self, id, name, balance, passport_number, age):
        self.is_id_unique(id)
        physical_person = PhysicalPerson(id, name, balance, passport_number, age)
        self.add_customer(physical_person)
        return physical_person
class LegalEntityFactory(CustomerFactory):
    def create_customer(self, id, name, balance, registration_number, tax_id):
        self.is_id_unique(id)
        legal_entity = LegalEntity(id, name, balance, registration_number, tax_id)
        self.add_customer(legal_entity)
        return legal_entity

class CompanyFactory(CustomerFactory):
    def create_customer(self, id, name, balance, industry, employee_count):
        self.is_id_unique(id)
        company = Company(id, name, balance, industry, employee_count)
        self.add_customer(company)
        return company

class Transaction:
    transaction_dict = {}
    
    def __init__(self, amount):
        self.transaction_id = None 
        self.transaction_type = None
        self.date = datetime.now()
        self.amount = amount
        self.details = []
    
    def is_id_unique(self,id):
        if id in Transaction.transaction_dict.keys():
            raise InvalidTransactionDataError("ID must be unique")
    
    def transaction_id_generator(self):
        t_id = []
        if self.transaction_type == "rental":
            t_id.append("01")
        elif self.transaction_type == "deposit":
            t_id.append("02")
        else:
            raise ValueError("Unidentified transaction type")
        t_id.append(str(datetime.now()).replace("-","").replace(" ","").replace(":","").replace(".",""))
        t_id.append(int(randint(10,99)))
        result = "".join(t_id)
        self.is_id_unique(result)
        self.transaction_id = result
    
    

class RentalTransaction(Transaction):
    def __init__(self, amount):
        super().__init__(amount)
        
class DepositTransaction(Transaction):
    def __init__(self, amount):
        super().__init__(amount)
class TransactionFactory(ABC):
    @staticmethod
    def add_transaction(transaction):
        Transaction.transaction_dict[transaction.transaction_id] = transaction
    
    @abstractmethod
    def create_transacrion(self,*args):
        pass

class RentalTransactionFactory(TransactionFactory):
    @staticmethod
    def create_transacrion(amount, days, customer_id, machine_id, daily_rate):
        transaction = RentalTransaction(amount)
        transaction.transaction_type = "rental"
        transaction.transaction_id_generator()
        transaction.details = [days,customer_id,machine_id,daily_rate]
        return transaction
        

class DepositTransactionFactory(TransactionFactory):
    @staticmethod
    def create_transacrion(amount, customer_id, payment_method):
        transaction = DepositTransaction(amount)
        transaction.transaction_type = "deposit"
        transaction.transaction_id_generator()
        transaction.details = [customer_id, payment_method]
        return transaction
class InvalidProductNameError(Exception):
    pass

class ProductNotAvailableError(Exception):
    pass

class InvalidCustomerDataError(Exception):
    pass

class InvalidProductDataError(Exception):
    pass

class InvalidTransactionDataError(Exception):
    pass

class MachineAlreadyRentedError(Exception):
    pass

class ClientNotFoundError(Exception):
    pass

class InvalidMachineTypeError(Exception):
    pass


# create_product(ExcavatorFactory(),"id1000","Bob Cat Excavator", 1000, 10, 1)
# create_product(CraneFactory(),"id2000","Bob Cat Excavator", 1000, 10, 1)
# create_product(DrillRigFactory(),"id3000","Bob Cat Excavator", 1000, 10, 1)

