#Assignment - Make A Calculator Program
'''
Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!
'''

a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))

print(f"Addition of {a} and {b} is",a+b)                 #Used f"" called as fString, it is used to directly refer the used variables using braces
print(f"Subtraction of {a} and {b} is",a-b)
print(f"Multiplication of {a} and {b} is",a*b)
print(f"Division of {a} and {b} is",a/b)
print(f"{a} raise to the power {b} is",a**b)
print(f"Floor Division of {a} and {b} is",a//b)