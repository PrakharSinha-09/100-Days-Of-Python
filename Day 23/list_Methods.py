listt=[2,3,4,6]
print(listt)

#append() method - appends anything @ the end of the list
listt.append(1)
print(listt)

#sort()
listt.sort()
print(listt)

listt.sort(reverse=True)            #sorting in descending order
print(listt)

#index() returns the index of a given number, if a number is not in the list, it will throw error.
print(listt.index(1))

#count()
print(listt.count(2))

# m=listt        Avoid Copying like this
# m[0]=3
# print(listt)        #yes original list changed, because line 21, conveys that the reference of listt is passed to m, so any changes made via m will get reflected in the original one too!
                    #so, it is better to use .copy() method to copy the list

#copy()
m=listt.copy()
m[0]=3
print(listt)      #this time, no change

#insert() method helps to insert the item at the provided index....and this list will increase by one
listt.insert(2,"Hey Prakhar")
print(listt) 

#extend() method adds an entire list or any other collection datatype(set,tuple,dictionary) to the existing list @ the end
m=[21,31]
listt.extend(m)
print(listt)   #this changes originial list "listt" right!...But What if, we want to concatenate, but keeping all these the seperate entity...
                #but it should be of same type only, i.e., it must be list too

#Using + operator to concatenate the list
k=listt+m
print(k)