class Product:   
    def __init__(self,name,types,price,):
        self.name = name
        self.types = types
        self.price = int(price)
    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}"
    
    def __repr__(self):
        return f"Product(object name = {self.name})"
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.name,self.types,self.price) == (other.name,other.types,other.price) 
        return False
    
class DigitalProduct(Product):
    def __init__(self, name, types, price, download_link):
        super().__init__(name, types, price)
        self.download_link = download_link
    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}, link for downloading: {self.download_link}"
    
class Cart:        
    def __init__(self):
        self.products = list()
    
    def add_product(self,product):
        self.products.append(product)
        print(f"You added {product.name} in your card")
    
    def __str__(self):
        return f"Your cart is: {self.products}"
    
    def __delitem__(self,index):
        print(f"{self.products[index]} was removed")
        del self.products[index]
    
    def __getitem__(self,index):
        print(f"{self.products[index]} is {index} in cart")
        return self.products[index]
    
    def __setitem__(self,index,item):
        print(f"Item {self.products[index]} was replaced by {item}")
        self.products[index] = item
        
    def __len__(self):
        print(f"Your ordered {len(self.products)} items")
        return len(self.products)
    
    def __bool__(self):
        if not self.products:
            print("Your cart is empty")
        else:
            print(f"Your cart has {len(self.products)} items")
        return bool(self.products)

class User:
    user_history_list = dict()
    
    def __init__(self,name,balance):
        self.name = name
        self._balance = int(balance)
    
    def __str__(self):
        return f"User name: {self.name}, balaance: {self._balance}$"
    
    def __gt__(self,other):
        if self._balance > other._balance:
            return f"{self.name}'s balance is greater then {other.name}"
        elif self._balance == other._balance:
            return f"{self.name}'s balance is equal then {other.name}"
        else:
            return f"{self.name}'s balance is less then {other.name}"
        
    def user_history(self):
        pass
        
    def checkout(self,card = None):
        summ = 0
        if card == None:
            print("Your card is empty")
        else:
            for items in card:
                summ += items.price
            if summ <= self._balance:
                self._balance -= summ
                card = None
                print(f"Payment was successful,payed: {summ}, curent balance: {self._balance}")
            else:
                print("You have not enought money on your balance")

# Testing stuff

# iphone = Product("iPhone 15", "smartphone", 1200)
# laptop = Product("MacBook Pro", "laptop", 2500)

# cart = Cart()
# cart.add_product(iphone)
# # print(cart)
# cart.add_product(laptop)
# # print(cart)

# print(len(cart))        # 2
# print(cart[0])          # iPhone 15
# print(bool(cart))       # True

# user = User("Alice", 5000)
# user.checkout(cart)     # Покупка с проверкой баланса

# print(user)             # Имя и остаток баланса