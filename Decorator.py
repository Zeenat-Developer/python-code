# # decorators is a functions that takes anothers function as an arguments and adds extra
# # functionality to the another function.
# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

def my_decorator(func):
    def wrapper():
        print("before the another function")
        func()
        print("after the function")
    return wrapper    

@my_decorator
def say_hallo():
    print("hallo word")

say_hallo()


# # def sqr(a):
# #     return a**2

# # # function as an argument
# # def square(func,l):
# #     new_list=[]
# #     for i in l:
# #         new_list.append(func(i))
# #     return new_list

# # numbers=[1,2,3,4,5]
# # print(square(sqr,numbers))

# # # function returing another function
# # def hello(msg):
# #     def inner():
# #         print(f"hello{msg}")
# #     return inner


# # var=hello("zeenat Ullah") # this functions returns inner and var will treat as an inner

# # var()

# def sqr(x):
#     def inner(n):
#         return f" the square is equal to {n**x}"
    
#     return inner

# square=sqr(3)
# print(square(2))


# def chat(msg):
#     def prntt():
# #         return f"hey what can i help you {msg}"
# #     return prntt

# # message=chat("zeenat Ullah")
# # print(message())

# # decorator is itself a function used to enhance the functionality of another function

# # def decorator(any_function):
# #     def wrapper_function():
# # #         print("this is awesone function")
# # #         any_function()
# # #     return wrapper_function    


# # # @decorator
# # # def func1():
# # #     print("this is function one")
# # # func1()  


# # # print("<......................>")

# # # @decorator
# # # def func2():
# # #     print("this is funciton two")
# # # func2()    

# # from functools import wraps
# # import time
# # def decorator(any_function):
# #     @wraps(any_function)
# #     def wrapper_function(*args,**kwargs):
# #         t1=time.time()
# #         print("this is awesone function")
# #         print(f"this is function {any_function.__doc__}")
# #         print(f"this is function {any_function.__name__}")
# #         t2=time.time()
# #         total_time=t2-t1
# #         print(f"it takes time in {total_time} seconds")
# #         return any_function(*args,**kwargs)
       
# #     return wrapper_function 

# # @decorator
# # def add(a,b):
# #     """  this function takes two numbers as an argument and return its sum"""
# #     return a+b

# # print(add(3,4))
# # print(add.__doc__)

# from functools import wraps
# def only_int_allowed(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         if all([type(arg)==int for arg in args]):
#             return any_function(*args,**kwargs)
#         else:
#             return "invalid arguments please try again later"
#     return wrapper_function

# @only_int_allowed
# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total

# print(add(1,2,3,4,5,"harshit")) 

# # decorators with arguments
# from functools import wraps
# def only_data_type_allowed(data_type):
#     def decorator(any_function):
#         @wraps(any_function)
#         def wrapper_function(*args,**kwargs):
#             if all([type(arg)==data_type for arg in args]):
#                 return any_function(*args,**kwargs)
#             else:
#                 return "invalide arguments"
#         return wrapper_function
#     return decorator


# @only_data_type_allowed(str) # decorator with argument
# def string(*args):
#     string=""
#     for i in args:
#         string+=i
#     return string

# print(string("harshhit"," vashishta")) 



