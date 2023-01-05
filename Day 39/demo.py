try:
    x = 1/0
    print(x)
except:
    print('Failed to set x')
else:
    print('No exception occured')                     #Since exception is raised, hence else will not get executed
finally:
    print('We always do this')