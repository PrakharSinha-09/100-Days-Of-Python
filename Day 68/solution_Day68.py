#Take this file Out Of Day 68 directory and keep it in 100DaysOfPython Directory, otherwise you will face error as of obvious reasons
#I've to push the code, so I've kept it combiningly in Day 68 directory
#And Of Course Don't forget to change the text file name in Day 68 directory to other names apart from something like that is present inside it
#otherwise it will throw error, again due to obvious reasons(as the file is already created, you can't create the file with same name)

import os

def clearClutter(extension):
    folders=os.listdir("/100DaysOfPython/Day 68")
    i=1
    for folder in folders:
        split_tup = os.path.splitext(folder)
        # file_name=split_tup[0]
        file_extension = split_tup[1]

        if(file_extension==extension):
            # os.rename(f"/100DaysOfPython/Day 68/{folder}",f"/100DaysOfPython/Day 68/{i}")
            os.replace(f"/100DaysOfPython/Day 68/{folder}",f"/100DaysOfPython/Day 68/{i}{extension}")
            i+=1

clearClutter(".txt")