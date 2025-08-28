# # LIST COMPREHENSION
# # used to create list in one line
# square=[i**2 for i in range(1,11)]
# print(square)

# def sqr(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square

# num=[1,2,3,4,5,6,7,8,9,10]
# print(sqr(num))   

# negative=[-i for i in range(1,11)]
# print(negative)

# names="ali khan" , "jawad khan"
# new_names=[name[0] for name in names]
# print(new_names)

# def negative(name):
#     neg=[]
#     for i in name:
#         neg.append(i[0])
#     return neg

# name=["aali khan","fawad kahan"]
# print(negative(name))   

# # list comphrehension with if statement
# even=[i for i in range(1,11) if i%2==0]
# print(even)

# even_odd=[i if i%2==0 else "not even" for i in range(1,11) ]
# print(even_odd)

# even=[i for i in range(1,11) if i%2==0]
# print(even)


# # a: list[int]=[1,2,3]
# # print(a)
# # a.append(a)
# # print(a[2][2])

# # numbers=[i if i%2==0 ]


# # NUMBER GUESSING GAME
# # import random
# # number=random.randint(1,100)

# # while True:
# #     try:

# #         ask=int(input("enter a number"))
# #     except:
# #         print("invalid input")

# # #         if ask==number:

# # #             print("you are the winner")

# # #             break

# # #         elif ask<number:

# # #             print("number is too low")

# # #         elif ask>number:

        
# # #             print("number is too high")

# # with list comprehension
# odd_nums=[i for i in range(1,11) if i%2!=0]
# print(odd_nums)

# # only with list
# def odd_nums(num):
#     output=[]
#     for i in num:
#         if i%2!=0:
#             output.append(i)
#     return output

# numbers=list(range(1,11))
# print(odd_nums(numbers))     


# # converts num to string 
# def num_to_str(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]

l=[True,False,1,1.2,"zeenat Ullah"]
# print(num_to_str(l))



# # list comprehension with if else 
# new_list=[i*2 if i%2==0 else -i for i in numbers]
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(new_list)

# nested_list=[[i for i in range(1,4)] for j in range(1,4)]
# print(nested_list)

# nested_list2=[["you are zeenat" for i in range(1,4)] for j in range(1,4)]
# print(nested_list2)

to_check=[i if type(i==int ) else "string" for i in l]
print(to_check)




