#Lets us see, how we can achieve inheritance..today we are going to see about single inheritance & multilevel inheritance

class Employee:
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"Name is {self.name} and id is {self.id}")

class Programmer(Employee):                                     #This measn that, programmer class is inherited from Employee class.
    def showSkills(self):
        print("Java, JS & Python")

#MultiLevel Inheritance
class Tester(Employee):
    def testing(self):
        print("I've the capability to test the software")
        

a=Employee("Prakhar",9)
a.showDetails()

p=Programmer("Prakhar",10)
p.name="Prakhar Sinha"
p.showDetails()
p.showSkills()

t=Tester("William Callaway",29)
t.name="William Callaway"
t.id=29
t.showDetails()
# t.showSkills()
t.testing()