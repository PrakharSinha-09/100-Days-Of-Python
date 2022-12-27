#Calculating Factorial
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))


#Calculating nth Fibonacci no.
def fibo(n):
    if(n==0 or n==1):
        return n

    return fibo(n-1)+fibo(n-2)

n=6
print(fibo(n))