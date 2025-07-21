raw_data = [
    "ноутбук:1200",
    "мышка:80",
    "монитор:300",
    "кабель:60",
    "клавиатура:150"
]

def log_maker(function):
    def inner_function(*args, **kwargs):
        print(f"function {function.__name__} in progress")
        result = function(*args, **kwargs)
        print(f"function {function.__name__} is completed")
        return result
    return inner_function

@log_maker
def dict_former(lists = raw_data):
    separated_list = list(item.split(":") for item in lists)
    new_dict = {key:int(value) for key,value in separated_list}
    print(new_dict)
    return new_dict

@log_maker
def price_filter(dictionary = None,price = 100):
    if dictionary == None:
        dictionary = dict_former()
    filtered_dict = {key:value for key,value in dictionary.items() if value>price}
    print(filtered_dict)
    return filtered_dict

@log_maker
def customer_list(dictionary = None):
    if dictionary == None:
        dictionary = price_filter()
    new_list = [f"{key} стоит {value}$" for key,value in dictionary.items()]
    print(new_list)
    return new_list

def lets_start():
    while True:
        command = input("Введити Вашу команду, чтобы вызвать список команд введите 'помощь': ")
        match command:
            case "выход":
                break
            case "помощь":
                print('''Список доступных команд: сформировать словарь, отфильтровать, результат.
                      Для выхода из программы введите "помощь". ''')
            case "сформировать словарь":
                dict_former()
            case "отфильтровать":
                prices = input("Введите цену товара: ")
                price_filter(price=prices)
            case "результат":
                customer_list()

lets_start()