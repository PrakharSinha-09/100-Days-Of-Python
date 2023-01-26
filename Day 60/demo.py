class MyClass:
    def __init__(self,value):
        self._value=value

    def showDetails(self):
        print(f"value is {self._value}")

    @property
    def ten_value(self):
        return self._value

    @ten_value.setter
    def ten_value(self,newvalue):
        self._value=newvalue*10

obj=MyClass(22)
obj.ten_value=60                #since @property decorator is used, the methods can be treated as like they are an attributes
# print(obj.value())
obj.showDetails()