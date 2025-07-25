from abc import ABC, abstractmethod
from datetime import date

class PaymentMethod(ABC):
    def __init__(self,name,amount,payed):
        self.name = name
        self.__amount = amount
        self.__payed = payed
    
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def validate(self):
        pass
    

class CashPayment(PaymentMethod):
    def pay(self):
        return self.__amount
    
    def validate(self):
        valid = self.__amount == self.__payed
        if valid: 
            print("Payment with Cash is successful")
        return valid

    
class CrdPayment(PaymentMethod):
    def __init__(self, name, amount, payed, card_number,data, cvv):
        super().__init__(name, amount, payed)
        self.__card_number = card_number
        self.__data = data
        self.__cvv = cvv
    
    def pay(self):
        return self.__amount
    
    def validate(self):
        card_number_valid = True
        cvv_valid = True
        data_valid = self.__data >= date.today()
        valid = card_number_valid and cvv_valid and data_valid and self.__amount == self.__payed
        if valid: 
            print("Payment with Card is successful")
        return valid

class PayPalPayment(PaymentMethod):
    def pay(self):
        return self.__amount
    
    def validate(self):
        valid = self.__amount == self.__payed
        if valid: 
            print("Payment with PayPal is successful")
        return valid

    
print(date(2026,5,4)>=date.today())