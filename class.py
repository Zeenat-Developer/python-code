# print("online entry test")
# class person:
#     def method(self,name,age):
#         self.name=name;
#         self.age=age;
#         if self.age<18:
#             return f"you are not eligible for entry test"
#         return f"you are eligible for entry test and your name is {self.name} and your age is {self.age}"

# obj=person()
# name=input("enter your name")
# age=int(input("enter your age"))
# print(obj.method(name,age))

# class student:
#     name="Zeenat Ullah"

# print(student.name)    
# del student.name
# print(student.name)


class person:
    def __init__(self,name,age,dob):
        self.name=name
        self.age=age
        self.dob=dob
        
        return f"your name is {self.name} and your age is {self.age} and date of birth{self.dob}"
        
class student(person):
    def __init__(self,rollno):
        self.rollno=rollno
        super().__init__(name, age, dob)

name=input("enter your name")
age=int(input("enter your age"))
dob=int(input("enter your date of birth"))
rollno=int(input("enter your roll number"))

obj_person= person(name,age,dob)

obj=student(rollno)
print(obj.__init__(name,age,dob))

    



