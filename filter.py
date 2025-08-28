# filter function is used to filter the elements in iterable based on a condition.
def is_even(a):
    return a%2==0

numbers=[1,2,3,4,5,6]
even=tuple(filter(is_even,numbers))
print(even)


words=["ali","jawad","fawad"]
long_words=list(filter(lambda word:len(word)>3,words))
print(long_words)
