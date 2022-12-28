s={2, 4, 6, 8}
print(s)

info = {"Tony", 19, False, 9.9, 19}
print(info)

#Creating Empty Set:
prakhar={}                   #Unfortunately, this will become dictionary, you can check its type too
print(type(prakhar))

#So, how to make an empty set ?
prakhar=set()                               #By doing this, we can achieve empty set.
print(type(prakhar))


#Accessing Set Items
for value in info:
  print(value)