def func():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0
 
  finally:                                          #firstly statements inside finally will be executed and then the value returned.
    print("I am always executed")
    # print("I am always executed")


x=func()
print(x)
