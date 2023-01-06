import random
ImportError
try:
  user = input("enter code or decode : ")
  if user == "code":
    code = input("Enter your word to code : ")
    
    if (len(code) >= 3):
      print("Your coded word is : ",code[::-1])

    else:
      frst_charac =   code[0]
      slic_e = code[1:]
      upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      lower_case = "abcdeghijklmnopqrstuvwxyz"
      user_for = upper_case+lower_case
      lenght = 3
      random_letter = "".join(random.sample(user_for,lenght))
      print("Your coded word is",random_letter + slic_e + frst_charac + random_letter)


  elif user == "decode":
    decode =input("Enter word decode it : ")

    if(len(decode)>=3):
      print("your decode word is : ",decode[::-1])

    else:
      print("Your decoded word is : ",decode[3:len(decode):-3])

except  Exception as o:
  print(o)