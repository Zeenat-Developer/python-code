# map function is used to apply a function on each element in iterable(list,tuple) etc

def sqr(a):
    return a**2

numbers=[1,2,4,5]
squared=list(map(lambda i:i**2,numbers))
squared1=list(map(sqr,numbers))
squared_length=map(len,numbers)
for i in numbers:
    print(i)



print(squared)
print(squared1)