from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self,name,amount,payed):
        self.name = name
        self.amount = amount
        self.payed = payed
    
    @abstractmethod
    def pay(self,amount):
        pass
    
    @abstractmethod
    def validate(self,payed):
        pass
    


    
    