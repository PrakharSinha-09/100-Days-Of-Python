#Integers are immutable
a=3
b=3
print(a is b)
print(a == b)

#Strings are also immutable
a="Hello"
b="hello"                            #See clearly string first character is small h, so they are not at all equal.
print(a is b)
print(a == b)

#Tuples are also immutable
a=(1,3,5)
b=(1,3,5)
print(a is b)
print(a == b)

#Lists are not immutable, thus in the case of a is b, they willl return false
a=[1,3,5]
b=[1,3,5]
print(a is b)
print(a == b)

#Sets, Dictionary are also not immutable