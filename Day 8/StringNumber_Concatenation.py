a=20
b="Prakhar"
#print(b+a)          this + operator as concatenation won't work in python as like other programming languages, doing so will throw error

#there are multiple ways to concatenate the two, lets see!

#Method 1 - Using str() function for number to typecast it in string
print(b+str(a))

#Method 2 - Using the % Interpolation Operator
print("%s%s" %(b,a))

#Method 3 - Using the str.format() function
print("{}{}".format(b,a))

#Method 4 - Using f-Strings                  #f-string internally converts in the strings
print(f'{a}{b}')