name = 'Prakhar'
for i in name:              #this in keyword is very important
  print(i)
  if(i =="k"):
    print("This is something special!")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k + 1)
  
# for k in range(1, 20001):               #this will print numbers from 1 to 20001-1
#   print(k)

  
for k in range(1,12, 3):               #third argument of range is called skip parameter, means how many numbers to skip b/w the provided ranges (here it is 1 to 12) means after 1 gets printed 4 will get printed then again 3 skips means 7 and so on!
  print(k)


for k in range(1,12):               
  print(k)