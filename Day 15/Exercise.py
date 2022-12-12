#Greet User according to the time like good morning, good evening etc
import time                                                 #time is inbuilt module in python
timestamp=time.strftime('%H:%M:%S')          #strftime returns string by default, so typecasted it in integer so that we can use it in exercise
# print(timestamp)
hour=int(time.strftime('%H'))
# print(timestamp)
min=int(time.strftime('%M'))
# print(timestamp)
sec=int(time.strftime('%S'))
# print(timestamp)
# print(type (timestamp))

user=input("Enter Your Name!")
if (hour>=0 and (hour<=11 and min<=59)):
    print("Good Morning ",user)


elif(hour>=12 and hour<=16):
    print("Good Afternoon ",user)

elif(hour>16 and hour<=19):
    print("Good Evening ",user)

else:
    print("Good Night ",user)

