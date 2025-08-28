my_dict={101:{"name":"zeenat","AGE":18,"COURSES":["physics","math","computer science"]},
         102:{"name":"khan","Age":78,"courses":["physics","math"]},
         103:{"name":"khan","Age":78,"courses":["physics","math"]},
         104:{"name":"khan","Age":78,"courses":["physics","math"]},
         105:{"name":"khan","Age":78,"courses":["physics","math"]}


         
         
         
    }
# print(my_dict[101]["name"])


# for rollno,info in my_dict.items():
#     print(f" Rollno is :{rollno}")
#     for key,value in info.items():
#         print(f"{key} : {value}")



# access data through indexing
# print(my_dict[101])

# pop method is used to return a value we pop

# pop method is used to delete the items as well as return the python
# poped_item=my_dict.pop(101)
# print(f"{poped_item}")

# # delete the data randomly
# popped_data=my_dict.popitem()
# print(f" popped data is : {popped_data}")

# del my_dict[101]
# print(my_dict)

# update method in python
# my_dict.update({"duration":"7 months","age":"45"})
# print(my_dict)

# # key method to find only key
# my_dict.keys()
# print(my_dict)

# # to find only values in python
# print(my_dict.values())

# use items method to find both keys and values
# # print(my_dict.items())

# # #  get method
# # print(my_dict.get(101))

# # print(type(my_dict))
# # print(len(my_dict))

# # # create dictionary through dict() method
# new_dict=dict(name="zeenat Ullah",age=18,courses=["physics","math","English"])

# # print(new_dict)

# for key in new_dict:
#     print(key)

# for value in new_dict.values():
#     print(value)    


# for key,value in new_dict.items():
#     print(f"here is your key   {key} and your values {value}  ")

# dict={101:{"name":"zeenat Ullah","age":18,"courses":["physics","math"]}}   

# print(dict[101]["name"])
# dict[101]["name"]="ali Muhammad"
# print(dict)

# # to add item in dict
# dict["duration"]="3 months"
# print(dict)


# create a dictionary from list using dic function and list comprehension
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

d = dict([(k, v) for k, v in zip(keys, values)])
print(d)

# keys=["fruits","fruits","fruits"]
# fruits_value=["apple","banana","strawberry"]

# dicts=dict([(k,v) for k,v in zip(fruit_keys,fruits_value)])
# print(dict)


#  get method is used to handle the error if there is key does not exist
students={"name":"zeenat Ullah","age":89}
print(students.get("location"))
print(len(students)) # return the how many keys and valus are exist












