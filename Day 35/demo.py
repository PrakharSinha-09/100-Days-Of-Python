for i in []:
    print(i)

else:
    print("List iS Empty")    


#Since break encountered, else statement will not execute!, same is true with while loop too!📌
for i in range(10):
    print(i)
    if i==4:
        break

else:
    print("Out Of the loop")    


#Since break encountered, else statement will not execute!, same is true with while loop too!📌
i=0
while(i<8):
    if(i==5):
        # break
        continue
    print(i)
    i+=1
else:
    print("Out Of Loop")