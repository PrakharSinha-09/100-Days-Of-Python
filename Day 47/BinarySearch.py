lis=[3,4,5,6,7,8,9,10,11,12]

elem=int(input("Enter Element TO Search"))

start=0
end=len(lis)-1
found=False

while(start<end):
    mid=(int)((start+end)/2)

    if(lis[mid]==elem):
        found=True
        break;
    
    elif(lis[mid]>=elem):
        end=mid-1

    else:
        start=mid+1


if(found):
    print(f"Got The ELement @ {mid} index")

else:
    print("Element Not Found!")


