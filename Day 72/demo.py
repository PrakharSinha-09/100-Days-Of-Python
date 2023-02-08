# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# class Programmer(Employee):
#   def __init__(self, name, id, lang):          #construcor calling of super class
#     super().__init__( name, id)
#     self.lang = lang

# rohan = Employee("Rohan", "420")
# prakhar = Programmer("Prakhar", "2345", "Python")
# print(prakhar.name)
# print(prakhar.id)
# print(prakhar.lang)

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()                   

child_object = ChildClass()
child_object.child_method()