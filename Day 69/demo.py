class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):                   #writing self is a standard however we can use write any name, by default it will refer to instance, but if we use decorator , classmethod, this self or or whatever is the first argument, will refer to the class.
    cls.company = newCompany


e1 = Employee()
e1.name = "Prakhar"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)            #to check if the class variable got changed or not, and yes it got changed!