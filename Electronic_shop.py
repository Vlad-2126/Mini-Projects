users = {}

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
        return "Your cart is empty" if not self.products else f"Your cart contains: {"".join(f"{i+1}. {p}" for i,p in enumerate(self.products))}"
    
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
    user_history_list = {}
        
    def __init__(self,name,balance,login,password):
        self.name = name
        self._balance = int(balance)
        self.login = login
        self.password = password
    
    def __str__(self):
        return f"User name: {self.name}, balaance: {self._balance}$"
    
    def __gt__(self,other):
        return self._balance > other._balance
    
    def compere_balance(self,other):
        if self._balance > other._balance:
            return f"{self.name}'s balance is greater then {other.name}"
        elif self._balance == other._balance:
            return f"{self.name}'s balance is equal then {other.name}"
        else:
            return f"{self.name}'s balance is less then {other.name}"
        
    def user_history(self):
        history = User.user_history_list.get(self.name, [])
        if not history:
            print("No purchase history")
        else:
            print("Purchase history")
            for item in history:
                print(item)
        
    def checkout(self,cart: Cart):
        summ = sum(p.price for p in cart.products)
        if summ <= self._balance:
            self._balance -= summ
            User.user_history_list[self.name] = cart.products.copy()
            cart.products.clear()
            print(f"Payment was successful,payed: {summ}, curent balance: {self._balance}")
        else:
            print("You have not enought money on your balance")

def program_start():
    while True:
        sign_in = input("Pleas enter your login if you are registered or create new account: ").lower()
        if sign_in == "create new account":
            user_data = ["",0,"",""]
            ready = False
            while ready is False:
                login = input("Pleas enter your new login: ")
                if login in users:
                    print("Your logi should be unique, try another one")
                    continue
                user_data[2] = login
                ready = True
            ready = False
            while ready is False:
                password = input("Pleas enter your new password: ") 
                while True:
                    password_check = input("Pleas enter your password again: ")
                    if password == password_check:
                        break
                    print("Incorrect, try again")
                    continue
                user_data[3] = password
                ready = True
            ready = False
            name = input("What is your real name: ")
            user_data[0] = name
            users[name] = user_data
            users[name] = User(user_data[0],0,user_data[2],user_data[3])
            

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