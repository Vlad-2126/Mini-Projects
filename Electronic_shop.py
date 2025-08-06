products_list = {}

class Product:   
    def __init__(self,name,types,price):
        self.name = name
        self.types = types
        self.price = int(price)
    
    @classmethod
    def create_product(cls,name,types,price):
        key = f"p{len(products_list)+1}"
        product = Product(name,types,price)
        products_list[key] = product

    
    def __str__(self):
        return f"Product: {self.name}, price: {self.price}"
    
    def __repr__(self):
        return f"Product(object name = {self.name})"
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.name,self.types,self.price) == (other.name,other.types,other.price) 
        return False

Product.create_product("IPhone 15","smartphone",1000)
Product.create_product("IPhone 14","smartphone",800)    
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
        
    def remove_product(self,product):
        self.products.remove(product)
        print(f"You removed {product.name} from your card")
    
    def __str__(self):
        return "Your cart is empty" if not self.products else "Your cart contains:\n"+"\n".join(f"{i+1}. {p}" for i,p in enumerate(self.products))
    
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
    
    def top_up_balance(self,amount):
        print(f"Your balance is now {self._balance + int(amount)}, previous balance was: {self._balance}")
        self._balance += int(amount)
    
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
            User.user_history_list[self.login] = cart.products.copy()
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
                login = input("Please enter your new login: ")
                if login in users:
                    print("Your logi should be unique, try another one")
                    continue
                ready = True
            ready = False
            while ready is False:
                password = input("Please enter your new password: ") 
                while True:
                    password_check = input("Please enter your password again: ")
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
                login = input("Please write your login: ")
                if login not in users:
                    print("There is no user with that login, try another one")
                    continue
                break
            while True:
                user = users[login]
                password_check = input("Please enter your password: ")
                if password_check != user.password:
                    print("There is no user with that login, try another one")
                    continue
                break
            while True:
                print(f"Hello {user.name}, how can I help you? If you want to see the list of commands, write 'help'")
                if login not in users_cart:
                    users_cart[login] = Cart()
                if login.login == "Admin":
                    print(f"Hello {user.name}, if you forgot admin's command ")
                command = input("Please write your command: ").lower()
                match command:
                    case "help":
                        for key,value in commands.items():
                            print(f"{key} - {value}")
                    case "products":
                        for value in products_list.values():
                            print(f"{value.name}: price is {value.price}$")
                    case "add product":
                        add_product = input("Witch product do you want to add?: ")
                        found = False
                        for product in products_list.values():
                            if product.name.lower() == add_product.lower():
                                users_cart[login].add_product(product)
                                found = True
                                break
                        if not found:
                            print("There is no such a product")
                    case "remove product":
                        remove_product = input("Witch product do you want to remove?: ")
                        found = False
                        for product in products_list.values():
                            if product.name.lower() == remove_product.lower():
                                users_cart[login].remove_product(product)
                                found = True
                                break
                        if not found:
                            print("Ther is no such item in your cart")
                    case "my cart":
                        print(str(users_cart[login]))
                    case "checkout":
                        user.checkout(users_cart[login])
                    case "top up balance":
                        amount = input("How much do you want to add to your balance?: ")
                        user.top_up_balance(amount)
                    case "history":
                        user.user_history()
                    case "log out":
                        break
                    case "admin's command":
                        if user.login == "Admin":
                            for key,value in admin_commands.items():
                                print(f"{key} - {value}")
                    case "add new product":
                        if user.login == "Admin":
                            add_product = input("Witch product do you want to add?: ")
                            add_price = input("Write price of this object: ")
                            add_type = input("Wich type thith object is?: ")
                            for p in products_list.values():
                                if p.name.lower() == add_product.lower():
                                    print("This product is already exist")
                                    break
                                else:
                                    Product.create_product(add_product,add_price,add_type)
                    case "remove old product":
                        if user.login == "Admin":
                            item_to_remove = input("Which item do you want to remove?: ")
                            found = False
                            key_to_remove = None
                            for key,item in products_list.items():
                                if item.name == item_to_remove:
                                    found = True
                                    key_to_remove = key
                                    break
                            if key_to_remove:
                                del products_list[key_to_remove]
                            if not found:
                                print("Ther is no such item in product list")
                    case "change curent product":
                        if user.login == "Admin":
                            item_to_change = input("Which item do you want to change?: ")
                            for key,item in products_list.items():
                                if item.name.lower() == item_to_change.lower() or key.lower() == item_to_change.lower():
                                    done = False
                                    while not done:
                                        property_to_change = input("Which parameter do you want to change?: ").lower()
                                        match property_to_change:
                                            case "name":
                                                name_to_change = input("Write new name")
                                                item.name = name_to_change
                                                is_it_done = input("Is it done or do you want to change other parametr?: ").lower()
                                                if is_it_done == "done":
                                                    done = True
                                                else:
                                                    continue
                                            case "type":
                                                type_to_change = input("Write new type")
                                                item.types = type_to_change
                                                is_it_done = input("Is it done or do you want to change other parametr?: ").lower()
                                                if is_it_done == "done":
                                                    done = True
                                                else:
                                                    continue
                                            case "price":
                                                price_to_change = input("Write new price")
                                                item.price = int(price_to_change)
                                                is_it_done = input("Is it done or do you want to change other parametr?: ").lower()
                                                if is_it_done == "done":
                                                    done = True
                                                else:
                                                    continue
                                            case "done":
                                                done = True