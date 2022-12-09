# slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start, if start index is not declared, it will take it by default as 0.
print(pie[5:])      #Slicing till End, if end index is not declared, it will go upto (length of string-1)
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
print(pie[0:-2])    #negative index is treated as length of string - (the value of end index provided) i.e., 8-2=6 means from 0 to 6(exclusive)
'''
Output:
Apple
Pie
pleP
ApplePie
'''


#whenever you get negative index, and get consfuse how to do it, just subtract that value with the length of string and whatever you get in positive, you will do it easily