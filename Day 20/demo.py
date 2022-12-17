def printSum(a, b):
  sum=a+b
#   print(sum)
  return sum

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass                      #since you have not written anything inside function, you cannot left it blank otherwise it will throw error(indentation errror), write pass keyword to supass the error 
  

a = 9
b = 8
isGreater(a, b)
print(printSum(a, b))

c = 8
d = 74
isGreater(c, d)
print(printSum(c, d))              #Since nothing is returned, from the function, and you are calling it inside print statement, it will throw error
