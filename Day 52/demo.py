# def square(x):
#     return x*x

#Exactly the same...read as lambda x and square the given x and then return it!
square=lambda x:x*x
print(square(3))

#lambda functions can have many no. of values!..lets see
avg=lambda x,y,z:(x+y+z)/3
print(int(avg(2,3,5)))

#Lamda expressions are mostly used when we deal with higher order functions...means when we deal with some function which accepts arguments as function and return the finction too!

def higherFunc(fx,value):
    return fx(value)+2                          #square of 2 will be calculated and increased to 2

print(higherFunc(square,3))
print(higherFunc(lambda x:x*x,3))               #this also does the same by using lamda function

#Why They are  called Anonymous Functions ?
#Because function doesn't have any name..right.For example we have made a function like which calculate the square but we haven't defined its name anywhere that's why there are called anonymous function