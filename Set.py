# # Set is unodered collection of unique items

# a={1,2,3,4,2}
# print(a)

# # adding data
# a.add(7)
# print(a)

# # removing data if present then return otherwise it will generate an error
# # a.remove(9)
# # print(a)

# # dicard method used to handle an error if not present the value
# a.discard(8)
# print(a)


# UNION 
s1={1,2,3}
s2={2,3,4,5}
print(s1 | s2)

# INTERSECTION
print(s1 & s2)

print(s1 ^ s2) # unique element 

print(s1 - s2)