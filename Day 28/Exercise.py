'''
Create a program capable of displaying questions to the user like KBC. 
Use List data type to store the questions and their correct answers. 
Display the final amount the person is taking home after playing the game.
'''

choice=input("Are You Ready To Play KBC Game ?...Answer iN Y or N \n")

#Taking Seven Questions
listQuestions=["Which Country Won FIFA World Cup 2022 ?","What Is The Capital Of India ?","What is Aryabhatt The Indian Scientist Known For ?","Which JS Framework is the most popular ?","Who is the founder of Apple","Who is The CEO Of Google ?"]

#Providing Options For Each Questions
listOptions=[["A. Argentina" ,"B. Portugal" ,"C. France", "D. Cruasia"],["A. Mumbai", "B. Delhi",  "C. Chennai", "D. Bangalore"],["A. Discovering Laws Of Motion", "B. DIscovering Zero", "C. Inventing Bulb", "D. Inventing Bulb"],["A. Angular", "B. React", "C. Vue", "D. NextJS"],["A. Aman Gupta", "B. Steve Jobs", "C. Piyush Bansal", "D. Mark Zukerberg"],["A. Larry Page", "B. Satya Nadella", "C. Sundar Pichai", "D. Parag Aggarwal"]]

#This is The List Of Correct Answers
listAnswers=["Argentina","Delhi","Discovering Zero","React","Steve Jobs","Sundar Pichai"]

#These Are The Price Money For The Respective Questions
listMoney=[1000,10000,20000,30000,50000,100000]             

#Actual Logic Starts Here📌
Winnings=0
if(choice=="Y"):

    for i in range(len(listQuestions)):
        print("Presenting You The First Question On The Screen! \n")
        print(listQuestions[i])
        print("Here Are The Options :)")
        print(listOptions[i][:])
        print("\n")
        print("Select Your Choice :\n")
        ans=input()
        choice1=input("Are You Sure To Proceed With The Answer ? Enter Y Or N \n")
        if(choice1=="N"):
            print("Select Your Choice :")
            ans=input()
        
        print("Computer G, Please Lock The Option")    
        if(ans==listAnswers[i]):
            print("Well Played! You Won",listMoney[i]+Winnings,"₹ \n")
            Winnings=Winnings+listMoney[i]

            choice2=input("Still Want To Continue with the Game ? Enter Y Or N....If You Lost in The Game, \nYou Will Not Win Any Amount!, If You Want To Quit, You Can and the amount you won till will be yours.")
            if(choice2=="N"):
                break

            else:
                continue

        else:
            Winnings=0  
            break 

    if(Winnings>0):
        print(f"Congrats! You Won {Winnings}"+"₹")  

    else:
        print("You Lost! Better Luck Next Time.")

else:
    print("Inorder To Play KBC, You Must Write Y!")




        
    
