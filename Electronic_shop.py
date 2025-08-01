class Product:   
    def __init__(self,name,types,price,):
        self.name = name
        self.types = types
        self.price = int(price)
        # products[self] = (self.name,self.types,self.price)
    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}"
    
    def __repr__(self):
        return f"Product(object name = {self.name})"
    
    def __eq__(self, value):
        return value == self.name
    
class Cart():        
    pass

class User:
    def __init__(self,name,balance):
        self.name = name
        self._balance = int(balance)
        self.card = None
    
    def __str__(self):
        return f"User name: {self.name}, balaance: {self._balance}$"
    
    def __gt__(self,other):
        if self._balance > other._balance:
            return f"{self.name}'s balance is greater then {other.name}"
        elif self._balance == other._balance:
            return f"{self.name}'s balance is equal then {other.name}"
        else:
            return f"{self.name}'s balance is less then {other.name}"
            
p1 = Product("iPhone 15", "smartphone", 1200)
p2 = Product("MacBook Pro", "laptop", 2500)






# iphone = Product("iPhone 15", "smartphone", 1200)
# laptop = Product("MacBook Pro", "laptop", 2500)

# cart = Cart()
# cart.add_product(iphone)
# cart.add_product(laptop)

# print(len(cart))        # 2
# print(cart[0])          # iPhone 15
# print(bool(cart))       # True

# user = User("Alice", 3000)
# user.checkout(cart)     # Покупка с проверкой баланса

# print(user)             # Имя и остаток баланса