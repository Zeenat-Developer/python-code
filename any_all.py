# l=[True,False,True,False]
# print(any(l)) # returns true if it least one element is true
# print(all(l)) # returns true if all elments are true

# nums = [4, 5, 6, 8]
# print(all(x > 3 for x in nums))  # True
# print(any(x > 7 for x in nums))  # True

# print(any(x>8 for x in nums))

# nums=[2,3,4,8,0] # zero is false
# print(any(nums))
# print(all(nums))

# print(all(i%2==0 for i in nums))
# print(any(i%2==0 for i in nums))


def func(name):
    return len(name)


# advanced min and max function
names=["zeenat Ullah","idrees"]
# print(max(names,key=func))
# print(min(names,key=func))
print(max(names,key=lambda item:len(item)))

students={
    "harshit":{"score":89,"age":34},
    "mohit":{"score":78,"age":87},
    "rohit":{"score":890,"age":44}
}

print(max(students,key=lambda item:students[item].get("score")))


print(max(students,key=lambda item:students[item].get("score")))
print(min(students,key=lambda item:students[item]["score"]))


guitars=[
    {"name":"ali","age":23,"address":"jhandi darsamand"},
    {"name":"jawad","age":34,"address":"hangu"},
    {"name":"Muhammmad","age":56,"address":"peshawar"}
]
print(sorted(guitars,key=lambda item:item.get("age")))
print(max(guitars,key=lambda item:item.get("age")))




