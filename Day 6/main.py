a=9
b="kmd"
c=True
d=None
print(type(a))      #to get the datatype
print(type(b))
print(type(c))
print(type(d))


e=complex(3,2)           #to create the complex number, we have complelx keyword in python...First argument is real part of number and the other is imaginary part

print(e,type(e))
 
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("IronMan", "Thor"), ("Jarvis", "Mionir"))
print(tuple1)

#the difference between list and tuple is that list is mutable(it can be changed) while tuple is unmutable(cannot be changed) 

dict1 = {"name":"Prakhar", "age":20, "canVote":True}
print(dict1)

#Concatenating Integer and Strings (One OF the way)
print("%s%s" %(b,a))         #by using the interpolation operator(%), we can concatenate integer and string in python