# Example of implicit type casting:
# Python automatically converts a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

'''
Ouput:
<class 'int'>
<class 'float'>
10.0
<class 'float'>
'''

a=2
b=3
#since a and b, both are numbers, they will be added (mathematically)
print(a+b)