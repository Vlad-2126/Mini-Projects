products_list = {}

class Product:   
    def __init__(self,name,types,price,):
        self.name = name
        self.types = types
        self.price = int(price)
        products_list["p"+str(len(products_list))] = [self.name, self.types, self.price]

    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}"
    
    def __repr__(self):
        return f"Product(object name = {self.name})"
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.name,self.types,self.price) == (other.name,other.types,other.price) 
        return False

p0 = Product("IPhone 15","smartphone",1000)
p1 = Product("IPhone 14","smartphone",800)    
class DigitalProduct(Product):
    def __init__(self, name, types, price, download_link):
        super().__init__(name, types, price)
        self.download_link = download_link
    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}, link for downloading: {self.download_link}"
    
class Cart:        
    def __init__(self):
        self.products = []
    
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
        history = User.user_history_list.get(self.login, [])
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

users = {"Admin":User("Oleg",1000000,"Admin","1234")} 
users_cart = {}
commands = {
    "help": "show all available commands", 
    "products": "show the list of currenyly available products",
    "add product": "choose product that will be added to your cart",
    "remove product": "choose product that will be removed from your cart",
    "my cart": "show the list of products in your cart",
    "checkout": "buy all your items from your cart when ready",
    "top up balance": "add money to your wallet",
    "history": "show a history of your orders",
    "log out": "log out program"
    }
admin_commands = {
    "admin's command": "show all available admin's commands",
    "add new product": "adding new product",
    "remove old product": "removing already existing product",
    "change curent product": "change already existing product"
}        

def program_start():
    while True:
        sign_in = input("Do you want to sign in or create new account: ").lower()
        if sign_in == "create new account":
            ready = False
            while ready is False:
                login = input("Pleas enter your new login: ")
                if login in users:
                    print("Your logi should be unique, try another one")
                    continue
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
                ready = True
            ready = False
            name = input("What is your real name: ")
            users[login] = User(name,0,login,password)
        elif sign_in == "exit":
            break
        else:
            while True:
                login = input("Pleas write your login: ")
                if login not in users:
                    print("There is no user with that login, try another one")
                    continue
                break
            while True:
                user = users[login]
                password_check = input("Pleas enter your password: ")
                if password_check != user.password:
                    print("There is no user with that login, try another one")
                    continue
                break
            while True:
                print(f"Hello {user.name}, how can I halp you? If you whant to see the list of commands, write 'help'")
                if login.login == "Admin":
                    print(f"Hello {user.name}, if you forgot admin's command ")
                command = input("Pleas write your command: ").lower()
                match command:
                    case "help":
                        for key,value in commands.items():
                            print(f"{key} - {value}")
                    case "products":
                        for value in products_list.values():
                            print(f"{value.name}: prise is {value.price}$")
                    case "add product":
                        if login not in users_cart:
                            users_cart[login] = Cart()
                        add_product = input("Witch product do you want to add?: ")
                        if add_product in products_list:
                            users_cart[login].add_product(products_list[add_product])
                    case "remove product":
                        pass
                    case "my cart":
                        pass
                    case "checkout":
                        pass
                    case "top up balance":
                        pass
                    case "history":
                        pass
                    case "log out":
                        break
                    case "admin's command":
                        if user.login == "Admin":
                            for key,value in admin_commands.items():
                                print(f"{key} - {value}")
                    case "add new product":
                        if user.login == "Admin":
                            pass
                    case "remove old product":
                        if user.login == "Admin":
                            pass
                    case "change curent product":
                        if user.login == "Admin":
                            pass
                        
                      

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