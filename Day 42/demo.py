lis = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for elem in lis:
#   print(mark)
#   if(index == 3):
#     print("Hey!")
#   index +=1

for index, elem in enumerate(lis, start=1):                #we can specify the index too from where you want to start the indexing
  print(elem)
  if(index == 3):
    print("Hey!")