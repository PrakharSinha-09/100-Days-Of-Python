class Person:
    def __init__(self,name,age) -> None:                        #this __init__ in python is called constructor method, which returns none
        self.name=name
        self.age=age

    def printInfo(self):
        print(f"My Name is {self.name} and my age is {self.age}")

if __name__=="__main__":
    a=Person("Prakhar",20)
    b=Person("Prabal",18)
    a.printInfo()
    b.printInfo()

#Constructors made are work simpe right!...hence it is recommended.