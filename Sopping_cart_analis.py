raw_data = [
    "ноутбук:1200",
    "мышка:80",
    "монитор:300",
    "кабель:60",
    "клавиатура:150"
]

def log_maker(function):
    def inner_funktion(*args, **kwargs):
        print(f"function {function.__name__} in progress")
        result = function(*args, **kwargs)
        print(f"function {function.__name__} is completed")
        return result
    return inner_funktion

@log_maker
def dict_former(lists = raw_data):
    separeited_list = list(item.split(":") for item in lists)
    new_dict = {item[0]:int(item[1]) for item in separeited_list}
    print(new_dict)
    return new_dict

@log_maker
def price_filter(dictionary = dict_former(),price = 100):
    pass