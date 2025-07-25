from abc import ABC, abstractmethod
from datetime import date

class PaymentMethod(ABC):
    def __init__(self,name,amount,payed):
        self.name = name
        self._amount = amount
        self._payed = payed
    
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def validate(self):
        pass
    

class CashPayment(PaymentMethod):
    def pay(self):
        return self._amount
    
    def validate(self):
        valid = self._amount == self._payed
        if valid: 
            print("Payment with Cash is successful")
        return valid

    
class CardPayment(PaymentMethod):
    def __init__(self, name, amount, payed, card_number,data, cvv):
        super().__init__(name, amount, payed)
        self.__card_number = card_number
        self.__data = data
        self.__cvv = cvv
    
    def pay(self):
        return self._amount
    
    def validate(self):
        card_number_valid = True
        cvv_valid = True
        data_valid = self.__data >= date.today()
        valid = card_number_valid and cvv_valid and data_valid and self._amount == self._payed
        if valid: 
            print("Payment with Card is successful")
        return valid

class PayPalPayment(PaymentMethod):
    def pay(self):
        return self._amount
    
    def validate(self):
        valid = self._amount == self._payed
        if valid: 
            print("Payment with PayPal is successful")
        return valid

    
class Order:
    def __init__(self):
        self.__items = []
        self.__total = 0
    
    def add_item(self,name,amount):
        self.__items.append((name,amount))
        self.__total += amount
        print(f"{self.__items} was added to your card, ammount: {self.__total}")
    
    def get_total(self):
        return self.__total
    
    def process_payment(self, method: PaymentMethod):
        print("/n=== Payment processing ===")
        if method.validate():
            print("Transaction is successfull")