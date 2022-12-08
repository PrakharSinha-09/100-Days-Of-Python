firstName ="Prakhar"
lastName='Sinha'

 
print("Hello, My Full Name is " ,firstName+" "+lastName)

#Multiline Strings
a = """Hey There
How are you, Hope You 
Are fine and doing well!."""
print(a)

#Accessing Each Character in the string via indexing
print(firstName[0])
print(firstName[1])
print(firstName[2])
print(firstName[3])
print(firstName[4])
print(firstName[5])
print(firstName[6])

print("Using for loop for the above purpose\n")          #We will se the concepts of loops in detail later...So Don't worry
for character in firstName:
    print(character)