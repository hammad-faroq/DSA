#Decorators uhnderstand
# def new_func(func):
#     def wrapper():
#         print("before the function!")
#         func()
#         print("after te function runs")
#     return wrapper


def my_func(*args, **kwargs):
    print("args:", args)       # tuple positional args
    print("kwargs:", kwargs)   # dictionary key word args

my_func(1, 2, 3, name="Hammad", age=20)
data = {"name": "Hammad", "gender": "male"}
my_func(1, 2, **data)