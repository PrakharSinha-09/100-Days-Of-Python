class Employee:
  companyName = "Apple"                       #class variable
  noOfEmployees = 0                           #class variable

  def __init__(self, name):
    self.name = name                           #all these are instance variables
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1

  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Prakhar")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" 
emp1.showDetails()  
#Employee.showDetails(emp1)                     line no. 16 & 17 are interpreted in the same way by the python interpreter...remember!
Employee.companyName = "Google"                 #yes we can change the class variables too!
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Adobe"
emp2.showDetails()