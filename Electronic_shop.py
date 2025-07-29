class Product:
    def __init__(self,name,price,types):
        self.name = name
        self.type = types
        self.price = price
    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}"
    
    def __repr__(self):
        return f"Product(object name = {self.name})"
    
    def __eq__(self, value):
        return value == self.name
    
    




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