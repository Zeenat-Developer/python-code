square={f" the square of {num} is ":num**2 for num in range(1,11)}
print(square)


name="zeenat"
name_dict={char:name.count(char) for char in name}
print(name_dict)

dictionary={i:"even" if i%2==0  else "odd" for i in range(1,11)}
print(dictionary)
