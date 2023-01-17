with open('file2.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('file1.txt', 'r') as f:
  print(f.read())