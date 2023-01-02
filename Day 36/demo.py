a=4
b=0
try:
    c=a/b                 #This will lead to zero division by error
    print(c)
except Exception as f:          #if you are not using e, you can avoid writing Exception as e(can be any letter).
    print(f)


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")