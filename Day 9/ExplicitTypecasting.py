# Example of explicit typecasting:
string="20"
number=7
string_num=int(string)             #throws an error if the string is not a valid integer
sum=number+string_num
print("The Sum of both the numbers is: ", sum)


a="34"
b="21"
print(int(a)+int(b))

'''
Output:
The Sum of both the numbers is 27
55
'''