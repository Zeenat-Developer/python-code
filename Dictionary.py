# # # Dictionary
# # # unordered collecton of data in key value pairs

# # students_info={"name":"zeenat Ullah","age":45,"location":"Jhandi Darsamand"}
# # print(students_info)

# # students_info["domicile"]="kpk"
# # print(students_info)

# # students_info.update({"district":"Hangu","Tehsil":"Thall"})
# # print(students_info)

# # students={"name":"jawad","age":3,"domicile":"kpk"}
# # print(students)
# # print(students.popitem()) # delete randomly

# # print(students.popitem())



# # # # students.update({"duration":"7 months","age":"45"})
# # # # print(students)


# # # # print(students)
# # # # # popped_item=students.pop("name")
# # # # # print(f"popped item is {popped_item}")
# # # # # students.popitem()
# # # # # print(students)

# # print(students_info["name"])

# # students_info={"name":"zeenat Ullah","age":45,"location":"Jhandi Darsamand"}
# # for i in students_info.items():
# #     print(i)
# # # # for i in students.keys():
# # # #     print(i)


# # # # for i in students.values():
# # # #     print(i)

# # # # for i in students.items():
# # # #     print(i)
# # # #     print(type(i))

# # # students={
# # #     101:{"name":"zeenat Ullah","age":18,"address":"darsamand tehsil thall"},
# # #     102:{"name":"Haizer","age":2,"address":"darsamand tehsil thall"},
# # #     103:{"name":"Hamid","age":6,"address":"darsamand tehsil thall"}

    
# # #     }
# # # print("students detail system")

# # students={
# #     101:{"name":"zeenat Ullah","age":89},
# #     102:{"name":"ali","location":"jhanid darsamand","age":78},
# #     103:{"name":"ahmad khan","location":"doaba","age":78}
# # }
# # print(students[101])


# # # print("<...................................................................>")

# # # for i in students.items():
# # #     print(i)

# # # print("find the student by entering rollno ")
# # # rollno=int(input("enter a rollno"))
# # # if rollno == 101:
# # #     print(f"full record of 101 student is {students[101]}")
# # # elif rollno==102:
# # #     print(f"full record of 102 student is {students[102]}")
# # # elif rollno==103:
# # #     print(f"full record of 103 student is {students[103]}")

# # # students_info=dict(name="ali",age=34)   
# # # print(students_info) 

# # students_dict=dict(name="zeenat",age=45)
# # print(students_dict)

# # # fruits=dict(name="ali",age=23,domicile="kpk")
# # # print(fruits)

# # user_infor={
# #     "name":"zeenat Ullah",
# #     "age":14,
# #     "fav_movies":["ali khan","shaheen darama","dadre morchal"]

# # }
# # print(user_infor)
# # # print(user_infor[2].append("pakistani daramas"))

# user_info={
#     "name":"waqas Muhammad",
#     "age":90,
#     "fav_movies":["pakistan daramas","turkey daramas"]
#      }

# user_info[2].append("uk daramas")
# print(user_info)

# # # if "name" in user_infor:
# # #     print("yes present")
# # # else:
# # #     print("not present")

# # # # to check values
# # # if 23 in user_infor.values():
# # #     print("yes present")
# # # else:
# # #     print("not present")

# # # for key,Value in user_infor.items():
# # #     print(key)
# # #     print(Value)

# # # <................IMPORTANT NOTES..........................>
# # # note in dictionary we have some keys that have same value so for that
# # # we use fromkeys function

# # # std=dict.fromkeys(["name","Age","domicile"],"unknown")
# # # print(std)


std=dict.fromkeys(["name","age","location"],"unknown")
print(std)


# # # get method is very useful if there is no key in dict then it will return none
# # # by default or you can give your own message like in below example "not found"
# # print(user_infor.get("namdome","not found"))


# # def cube(n):
# #     output={}
# #     for i in range(1,n+1):
# #         output[i]=i**3
# #     return output

# # print(cube(10))

# # def word_counter(word):
# #     count={}
# #     for char in word:
# #         count[char]=word.count(char)
# #     return count

# # word=input("enter any word")
# # print(word_counter(word))


# # # adding data in empty dictionary
# # students_Details={}

# # students_Details["name"]="ali khan"
# # students_Details["age"]=12
# # students_Details["domicile"]="kpk"

# # print(students_Details)

def word_counter(word):
    count={}
    for char in word:
        count[char]=word.count(char)
    return count

word=input("enter any word")
print(word_counter(word))

students=dict.fromkeys(["name","Age","location"],"unknown")
print(students)


