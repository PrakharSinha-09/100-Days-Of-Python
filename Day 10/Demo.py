a=input("Enter Your Name :")                  
print("My Name is ",a)

'''
Output:
Enter Your Name :
Prakhar
My Name is Prakhar
'''

x=input("Enter First Number")
y=input("Enter Second Number")
print(x+y)                            #output will be 23(if first number is 2 and the second number is 3),as we have discussed earlier that by default, input is in String format, hence concatenation is performed....So No Surprises!



x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
print(x+y)                             #output will be 5 (if first number is 2 and the second number is 3),as now we have typecasted the variable into integer so normal addition will be performed
