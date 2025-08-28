# simple calculator
# def add_two(a,b):
#     if operator=='+':
#         return a+b
#     elif operator=='-':
#         return a-b
#     elif operator=='-':
#         return a*b
#     elif operator=='-':
#         return a%b
#     else:
#         return "invalid state"
    

# num1=int(input("enter a first number"))
# operator=input("enter an operator")
# num2=int(input("Enter a 2nd number"))
# sum=add_two(num1,num2)
# print(sum)

# def add_two_numbers(name):
#     if name=="zeenat Ullah":
#         return "you are the winner"
#     return "you are not zeenat Ullah"

# student_name=input("enter your name")
# print(add_two_numbers(student_name))


# # function returns last character
# def returns_last(student_name):
#     return student_name[8]
# print(returns_last("character"))
    


def ask_name(name,age):
        if age>=18:
            return f"{name} you are eligible"
        return f"{name} you are not eligible"

    
student_Name=input("enter your name")
student_Age=int(input("Enter your age"))
print(ask_name(student_Name,student_Age))




