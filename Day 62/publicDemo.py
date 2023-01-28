class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(20,"Prakhar")
print(obj.age)
print(obj.name)