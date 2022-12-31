#update() method, via this method, you can update any value of the key or you can add new key-value too!
info = {'name':'Prakhar', 'age':19, 'eligible':True}
print(info)

info.update({'age':20})
info.update({'DOB':2002})
print(info)

#clear() method empties the dictionary entirely
info.clear() 
print(info)

#pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name':'Prakhar', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#popitem() method deletes last key-value from the dictionary.
info = {'name':'Prakhar', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

#del keyword, remember it is not a function, its a keyword to remove a dictionary item.
del info['age']
print(info)

#If key is not provided, then the del keyword will delete the dictionary entirely.

