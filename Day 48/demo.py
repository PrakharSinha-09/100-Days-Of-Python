x=9
print(x)

def fun():
    global x                                                #You can directly initialize like global x=8, this will be error..This Simple means catch the global variable x via preceding it via global keyboard
    x=8                                                     #Updating Now!
    print(f"Local Value oF x is {x}")              

fun()
print(f"The Global Value of x is {x}")                      #Global Variable will also change to 8