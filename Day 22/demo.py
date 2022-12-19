list1=[2,3,4,"3"]
print(list1)
print(type(list1))
print(list1[2])        #accessing through index

#list can be changed, while tuple cannot be changed
list1.append(2)
print(list1)

#Negative indexing, as we did in strings
print(list1[-2])              #if you encounter with any sort of confusion, then convert the index in the posive index as we did in the case of strings.


#checking if a particular element is in the list or not.
if "3" in list1:
    print("yes it is present")
else:
    print("Nope")

#Same thing applies for Strings too!
if "Pr" in "Prakhar":
    print("Yes")
else:
    print("No")


#printing entire list, 2 simple ways
print(list1)
print(list1[:])          #this is equivalent to list1[0:len(list1)]

#Slicing is also possible in the list
print(list1[1:5:2])       #Will Start from index 1, and then directly jump to current index+2 till 5

#List Comprehension
lst=[i for i in range (10)]
print(lst)
lst=[i+i for i in range (10)]
print(lst)
lst=[i+i+i for i in range (10) if (i+i+i)%2==0]   #we can include multiple statements in th list comprehension
print(lst)