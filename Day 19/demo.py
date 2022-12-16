#print table of 5 upto 10 times
for i in range(15):
    if i>10:     
        break               #this  means that once we i becomes greater than 10, it will break the loop and come out of it
    print(5*i)

#Continue Statement
for i in [2,3,4,6,8,0]:
    if (i%2!=0):                            #if a number is not an even number, it will be skipped for printing...Thats what a continue statement does.
        continue
    print(i)    