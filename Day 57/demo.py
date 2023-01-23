class Person:
    name="Prakhar"
    age=20
    Course="BTech"

    def printDetails(self):                            #self is the keyword, which refers to the current class object, like in this case self is same as object "a"..but you cannot write a there...or in simeple words in hindi self is that object jiske liye method is getting called
        print(f"Name is {self.name}, age is {self.age} and the course is {self.Course}")


a=Person()                                  #a is the object of Person class.
print(a.name)  
a.name="Prabal"                             #We can change it here too

b=Person()
b.name="Rohan"
b.age=34
b.Course="MBA"

print(a.printDetails())
print(b.printDetails())


#We can make as many objects out of a class as we want!