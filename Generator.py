# # generators are iterator
# # in case of generator in memory at a time one element is stored and print and this 
# # element will disappear once it prints then another wll generate and print and so on.
# # less memory used.
# # less time.
# # generator is  best when you used element only one time.

# # def count_up_to(n):
# #     count = 1
# #     while count <= n:
# #         yield count
# #         count += 1

# def even(n):
#     for i in range(1,n+1):
#         yield i

# print(even(6)) 

# for i in even(6):
#     print(i)

# # numbers=count_up_to(5)
# # print(numbers)

# # for num in numbers:
# # #     print(num)


# # # for num in numbers:
# # #     print(num)


# # def num(n):
# #     for i in range(1,n+1):
# #         yield i

# # print(num(5))

# # for a in num(5):
# #     print(a)

# def even_generator(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i

# print(even_generator(5)) 

# for i in even_generator(5):
#     print(i)

# for i in even_generator(5):
#     print(i)    

# # for i in even:
# #     print(i)


# # # # generator comprehension
# # # import time
# # # t1=time.time()
# # # numbers=(i**2 for i in range(1,11))
# # # t2=time.time()
# # # total_time=t2-t1
# # # print(total_time)

# # # t3=time.time()
# # # numbers=[i**2 for i in range(1,11)]
# # # t4=time.time()
# # # total_time2=t4-t3
# # # print(total_time)
    
# # # generator comprehension is same as list comprehension but here just used  () this bracket
# numbers=(i**2 for i in range(1,6))
# print(numbers)

# for i in numbers:
#     (i)
# # for i in numbers:
# #     print(i)

even=(i/2==0 for i in range(1,6))
print(even)

# for i in even:
#     print(i)

for n in even:
    print(n)

# def even_generator(l):
#     for i in l:
#         if i%2==0:
#             yield i


# numbers=[1,2,3,4,5]
# print(even_generator(numbers))

# for i in even_generator(numbers):
#     print(i)


# even=(i%2==0 for i in range(1,10))

# for i in even:
#     print(i)