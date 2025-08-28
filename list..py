# list is mutable and allow duplicate values
# my_info=[1,2,3,"Muhammad"]
# print(my_info[0])

# my_info=[1,2,3,4,5,"Zeenat Ullah"]
# # print(my_info)
# # print(my_info[0])
# # my_info.append("ali")
# # print(my_info)
# my_info.insert(0,"i am a data scientist")
# print(my_info)

# add item in list
# my_info.append("cnic") # append() it adds item at the end
# print(my_info)

# # insert method to add item where we want
# my_info.insert(2,"domicile")
# print(my_info)

# Fruit1=["orange","grapes"]
# Fruit2=["apple","banana"]
# # Fruits=Fruit1+Fruit2
# # print(Fruits)

# # extend method is used to add the elements of one list to another list
# Fruit1.extend(Fruit2)
# print(Fruit1)
# print(type(Fruit1))

# students=["ali","jawad khan","amir wali khan"]
# students_1=["khan","ali","iqbal khan"]

# # students.extend(students_1)
# # print(students)

# # students.append(students_1)
# # print(students)

# # # pop method delete and return 
# # Fruit1.pop(0)
# # print(Fruit1)
# students.pop()
# print(students)

# # # delete operator
# # del Fruit1[1]
# # print(Fruit1)
# del students[0]
# print(students)

# # # # reomve method
# # # # Fruit1.remove("banana")
# # # # print(Fruit1)
# # students.remove("jawad khan")
# # print(students)

# # sorted function is used for ordering
# # vegetables=["tomatoes","potatoes","onion"]
# # print(sorted(vegetables)) 

# # fruits=["banana","mangoes","apple"]
# # # print(sorted(fruits))

# # if "apple" in fruits:
# #     print("yes present")
# # else:
# #     print("not present")



# # numbers=[1,3,4,2]
# # print(sorted(numbers))

# # if 1 in numbers:
# #     print("yes present")
# # else:
# #     print("not present")



# # # # clear method
# # # print(numbers.clear())



# # # # # copy method
# # # # print(Fruit1.copy())
 
# # # # # convert string into list
# # # # names="khan","jawad".split(",")
# # # # print(names)

# # # convert string into list
# # name="zeenatUllah","alikhan".split(",")
# # print(name)



# # print(",".join(name))

# # # # list inside the another list
# # # matrix=[[1,2,3],[3,4,5]]
# # # print(matrix[0][1])

# mixed_fruits=[["ali","jawad khan","amir khan"],["this is me","hashim","noor"]]
# # print(mixed_fruits[0][0])
# # looping in list
# # fruits=["apple","mangoes","banana"]
# # for i in fruits:
# #     print(i)
# # # # loop in list
# # # user_info=[1,2,3,4]
# # # for i in user_info:
# # #     print(i)

# # for i in ["ali","khan"]:
# #     print(i)

# # # # # list function
# # # # numberss=list(range(1,10))
# # # # print(numberss)

# # # numbers=list(range(0,12))
# # # print(numbers)
# # # vegetables=list(("tomatoe","onion","lady finger"))
# # # print(vegetables)

# # # if "tomatoe" in vegetables:
# # #     print("yes it is present")
# # # else:
# # #     print("not present")


# # students_details="zeenat","Ullah","domiclie and cnic".split(",")    
# # print(list(students_details))
# # print(type(students_details))

# # print(students_details[0:2])

# # # this_List=["apple","banana","strawberry","grapes"]
# # # print(len(this_List))
# # # my_list=this_List[:]
# # print(len(students_details))


# # # my_list=this_List.copy()
# # # print(my_list)

# # my_list=["ali","khan","jawad"]
# # my_list_2=my_list.copy()
# # print(my_list_2)
# # print(my_list)


# # # my_list.clear()
# # # print(my_list)


# # # index method return the index of the values on what positon it is located it means find the i
# # # index of the value
# # # print(this_List.index("apple"))

# # # print(my_list_2.index("ali"))
# # print(my_list.index("jawad"))


# # # print(this_List[-4:-2])

# # #  add items in list
# # # this_List[1:2]="ali","khan"
# # # print(this_List)

# # my_list[0:3]="ali","MUHAMMAD","jawad"
# # print(my_list)


# # you can add tuple inside list
# this_list=["jawad","ali","khan"]
# this_tuple=("ali","jawad","hamid")
# print(this_list)
# this_list.extend(this_tuple) # will just extend the list it means add the elements of one list inside the another list
# print(this_list)

# for i in this_list:
#     # print(this_list[i])
#     print(i)

# # for i in range(len(this_list)):
# #     print(this_list[i])    

# # for i in this_List:
# #     print(i)

# # looping through indexing
# # for i in range(len(this_List)):
# #     print(this_List[i])   

 


# # i=0
# # while i<len(this_List):
# #     print(this_List[i])
# #     i=i+1

# i=0
# while i<len(this_list):
#     print(this_list[i])
#     i+=1

# # == and is 
# fruits=["orange","apple","pear"]
# fruits2=["banana","mangoes","apple"]
# check the memory location
# print(fruits is fruits2) 
# # check if two lists are same
# print(fruits == fruits) # True 
# print(fruits is fruits2) 
# print(fruits == fruits)         

# accessing list inside list
# matrix=[[1,2,3],[3,4,5],[6,7,8]]
# for sublist in matrix:
#     for i in sublist:
# #         print(i)
# # matrix=[[1,2,3],[3,4,5],[5,6,7]]
# # print(matrix[0][0])

# # for sublist in matrix:
# #     for i in sublist:
# #         print(i)
# # # print(matrix[0][0])

# # # numbers=list(range(1,11))
# # # print(numbers)

# # # # show index
# # # print(numbers.index(1))

# # numbers=[1,2,3,4,5,6,7]
# # # print(numbers.index(1,2)) # index(value,start_position,end_positon)
# numbers=[1,2,3,4,5,6,7,5]
# # print(numbers.index(5,5))  # index(value,start_position.end_position)

# #  # write a function to return negative numbers

# # # # def negative_list(numbers):
# # # #     negative=[]
# # # #     for i in numbers:
# # # #         negative.append(-i)
# # # #     return negative    

# # # # print(negative_list(numbers))   
# def negative_list(numbers):
#     negative_list=[]
#     for i in numbers:
#         negative_list.append(-i)
#     return negative_list

# print(negative_list(numbers))  
        


# # def square(numbers):
# #     square=[]
# #     for i in numbers:
# #         square.append(i**2)
# #     return square

# # print(square(numbers))  

# def square_list(numbers):
#     square_list=[]
#     for i in numbers:
#         square_list.append(i**2)
#     return square_list

# print(square_list(numbers))    



# # # def reverse_list(numbers):
# # # #     rev_list=[]
# # # #     for i in range(len(numbers)):
# # # #         popped_item=numbers.pop()
# # # #         rev_list.append(popped_item)
# # # #     return rev_list

# # # number
# s=[1,2,3,4,5,6]
# # # print(reverse_list(numbers))    

# # def reverse_list(numbers):
# #     numbers.reverse()
# #     return numbers

# # print(reverse_list(numbers))

# def reverse_list(numbers):
#     return numbers[::-1]

# print(reverse_list(numbers))


# # def reverse_string(fruits):
# #     fruits=[]
# #     for i in fruits:
# #         fruits.append(i[::-i])
# #     return fruits

# # fruits1=["apple","banana","pear"] 
# # print(reverse_string(fruits1))   

fruits=["apple","banana","mangoes"]

def reverse_string(fruits):
    reverse_string=[]
    for i in fruits:
        reverse_string.append(i[::-1])
    return reverse_string

print(reverse_string(fruits))    


numbers=[1,2,3,4,5,6,7,8,9]

def odd_even(numbers):
    odd=[]
    even=[]
    for i in numbers:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

print(odd_even(numbers))        
            

# def odd_even(numbers):
#     even = []
#     odd = []
#     for i in numbers:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even,odd
    

# numbers = [1, 2, 3, 4, 5, 6]
# print(odd_even(numbers))

# # find the commond element between two lists
# def common_element(l1,l2):
#     output=[]
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output

# l1=[1,2,3]
# l2=[1,2,4]     
# print(common_element(l1,l2))   

list1=range(1,11)
list2=range(6,11)

def common_element(list1,list2):
    output=[]
    for i in list1:
        if i in list2:
            output.append(i)
    return output

print(common_element(list1,list2))        

# print(min(l1))
# print(max(l1))


# numbers=[1, 2, 3, 4, 5, 6]

# def odd_Even(numbers):
#     odd=[]
#     even=[]
#     for i in numbers:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return odd,even
# print(odd_Even(numbers))


# def sublist_counter(l):
#     count=0
#     for i in l:
#         if (type(i)==list):
#             count=+1
#     return count

# l=[1,2,3],[1,2,4],[4,5,6]
# print(f"counting in {sublist_counter(l)}")  
# 
def sublist_counter(l):
    count=0
    for i in l:
        if (type(i)==list):
            count+=1
    return count

l=[1,2,3],[3,4,5],[5,6,7]
print(f"there is {sublist_counter(l)} lists ")
        




        



















