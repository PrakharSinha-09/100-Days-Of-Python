#To be honest, we cannot manipulate a tuple directly...we have to do it
#indirectly by converting it to the list and then converting back to the tuple.
#for example:

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)                       #converting to the list
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)                     #converting back to the tuple.
print(countries)

#Concatenation
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#count() method
tup=(2,4,5,6,7,8,9,9)
print(tup.count(3))

#index() method returns the index of first occurence of the given number, if a number provided is not in the tuple, it will throw  value error.
print(tup.index(2))

#if we want to see in some sub tuple, we can do it too by slicing
print(tup.index(6,3,6))               #first argument is, number you want to serach, second arg is the starting index and lastly we have end index

print(len(tup))