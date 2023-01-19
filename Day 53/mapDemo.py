#When We Are Concerned that For *every element of list*, we want some function to execute
#We have naive way to do that as well, but using map, you can achieve that just in 1 line.

def cube(x):
    return x*x*x

ls=[2,3,5,7,4,2]
lst=[]

for item in ls:
    lst.append(cube(item))

print(lst)

#Via Map...here map object is returned which can further by typecasted into lists or tuple or any iterable
lst1=tuple(map(cube,ls))
lst1=list(map(cube,ls))
print(lst1)
