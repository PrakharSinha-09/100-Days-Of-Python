lis=[3,4,5,2,5,7,21,9]
elem=int(input("Enter Element TO Search"))

found=False
for i in range(len(lis)):
    if lis[i]==elem:
        found=True
        break

if(found):
    print(f"Element Found @ {i}")

else:
    print("Element iS Not Present")
