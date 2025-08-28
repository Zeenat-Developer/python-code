# zip function is used to join two lists together.
user_id=["user 1","user 2","user 3"]
names=["zeenat Ullah","ali Muhammad","jawad khan"]

emp_info=list(zip(user_id,names)) # it returns a list of tuples
print(emp_info)

# * operator with zip
num1=[1,3,5]
num2=[2,4,6]

# result=list(zip(num1,num2))
# print(result)
# print(list(zip(*result)))

# maximum element in each pair
# new_list=[]
# for pair in zip(num1,num2):
#     new_list.append(max(pair))
# print(new_list)    

# # average finder
# def average_finder(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
# num1=[1,3,5]
# num2=[2,4,6]
# print(average_finder(num1,num2))

average_finder= lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder(num1,num2))




    





