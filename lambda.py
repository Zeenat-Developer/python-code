# # lambda expression or lambda function is an anonymous function in python
# add=lambda a:a**2
# print(add(3))


# def add1(a):
#     return a**2

# print(add1(3))

# add2=lambda a,b: f"{a} is greater than {b}" if a>b else "{b} is greater than {a}"
# print(add2(2,3))

# names=["zeenat","ali","jawad"]
# name=lambda names:[name[0] for name in names]
# print(name(names))

# numbers=[1,2,3,4,5,6]
# is_even=lambda numbers:[i for i in numbers if i%2==0]
# print(is_even(numbers))

names=["zeenat","ali"]
is_present=lambda names:"yes present" if "zeenat" in names else "not present"
print(is_present(names))



