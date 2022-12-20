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

m=listt
m[0]=3
print(listt)        #yes original list changed, because line 21, conveys that the reference of listt