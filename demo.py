x=int(input("Enter A Number"))
match x:
    case 1:print("Number is 1")
    case 2:print("Number is 2")
    case 3:print("Number is 3")
    case 4:                                                    #just to understand how can we use if-else in match case statements😁
        if x%2==0:
            print("4 is even")
        
        else:
            print("4 is odd")

    case _ if x!=5:print("x is not 5")
    case _:print("Dosen't matched with above cases")            #we use underscore(_) to represent default in python unlike other programming languages, we don't have default keyword here.



#Remember:
'''
1- We don't need to write break statement here, as we used to do in other languages, because in python only the matched cases are executed!
2- We use underscore for providing default functionality
3- We can have multiple defaults with the help of if statements    (See Above)
'''



#Doubtful ? Feel Free to Ask!