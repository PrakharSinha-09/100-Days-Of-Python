class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        self.name=name
        
    def __funName(self):  # An indication of private function
        self.y = 34
        print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject(22,"qed")

# calling by object of class Student
# print(obj.__age)
# print(obj.__funName())

# calling by object  of class Subject
# print(obj1._Subject__age)                  //Will give error in everycase if we try to access from the subclass.
# print(obj1.__funName())

#This is how we can access the private attributes too! via mangling
print(obj._Student__age)
obj._Student__funName()



