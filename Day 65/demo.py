class Math:
    def __init__(self,num) -> None:
        self.num=num

    def addTonum(self,n):
        self.num=self.num+n
        print(self.num)

    @staticmethod 
    def subtract(a,b):                   #Noticed one Thing, that here while creating the methods, we are not using self keyword, it is because it is a static method, which doesn't have anything to do with the instance of the class.
        return a-b

a=Math(5)
a.addTonum(3)
print(a.subtract(50,45))                #Since subtract is a static method, we can call it via its class name too!
print(Math.subtract(50,45))  


#Noticed one Thing, that here while creating the methods, we are not using self keyword, it is because it is a static method, which doesn't have anything to do with the instance of the class...
#So, Remember One Thing that we can create methods without self keyword too as long as it is a static method...and this is one of the very important interview question too!

#Interviewer Might Ask you is it possible to create methods in python without passing self as an argument in the methods ?
#So, the answer is YES, if we create that method as a static method