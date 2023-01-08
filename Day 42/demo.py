lis = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for elem in lis:
#   print(mark)
#   if(index == 3):
#     print("Hey!")
#   index +=1

for index, elem in enumerate(lis, start=1):                #we can specify the index too from where you want to start the indexing
  print(elem)
  if(index == 3):
    print("Hey!")
    

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))
