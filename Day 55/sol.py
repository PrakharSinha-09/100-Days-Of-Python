# Let us take an assumption that :
'''
1 Represents Rock
2 Represents Paper 
3 Represents Scissor
'''

import random

player=int(input("Select Your Choice: 1-Rock, 2-Paper, 3-Scissor \n"))
computer=random.randint(1,3);
print("Computer Choice: ",computer)

if(player==computer):
    print("Game Draw")


if((player==1 and computer==3) or (player==2 and computer==1) or (player==3 and computer==2)):
    print("Player Wins!")

else:
    print("Computer Wins!")


