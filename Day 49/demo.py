file=open('demoFile.txt','r')          #r mode is default!..if we don't write r, it won't throw error
text=file.read()
print(text)
file.close()

#Wriring A File
file=open('demoFile.txt','w')                           #While we write using w mode, it will overwrite the existing texts.
file.write("Hey How Are You ?")
file.close()                                           #closing the file is mandatory!...in case of appending i.e., opening file i a mode or w mode

#You Can Choose to skip the filw, if ypu use with keyword...Lets See How!
with open('demoFile.txt','w') as file:
    file.write("Using With Keyword, You No Longer Need to close the opened file, inorder to reflect the changes made.")
    
file=open('demoFile.txt','a') 
file.write("The write method also works as the appending, if you have opened the file in a mode")