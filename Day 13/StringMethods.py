#Remember that Strings are immutable(cannot be changed)
#that means whatever operations, that are performed on strings, it creates new strings.

a="prakhar!!! john williams"
print(a)


#len method - to get the length of string
print(len(a))


#upper() method - to convert string in the upper case
print(a.upper())


#lower() method - to convert string in the lower case
print(a.lower())


#rstrip("delimmiter") method - to remove trailing delimmiter
print(a.rstrip("!"))           #this only removes trailing characters and not the preceding characters.


#replace("whattoReplace","with what") - to replace
print(a.replace("Prakhar","Rohit"))


#split method - this will convert strings into list on the basis on what have been set as a delimmiter.
print(a.split(" "))     #delimitter here is spaces, thus wherever space is getting encountered, splitting is done to get list of string.As you can see in the output


list=a.split(" ")
print(list)


#capitalize() method - converts only first character to upperCase and remaining to the lower case.
s="hello World"
print(s.capitalize())


#center(no. required) method - aligns string to the center as per the argument passes inside no. required
print(len(s))
print(s.center(50))
print(len(s.center(50)))

print(s.center(50,"e"))   #We can also provide padding character. It will fill the rest of the fill characters provided by the user.


#count("") method - to count the occurence of a particular word in the given string
n="This is Prakhar Sinha's Repository, Prakhar is Currently 3rd Year UG Student"
print(n.count("Prakhar"))      #Prakhar is present 2 times in the string


#endswith("") method - to check if the particular string is ending with the provides argument string or not
print(n.endswith("Student"))
#we can even check if the value in between the string by providing the starting and ending index, if it endswith the relevant, it will print true otherwise false
str="Welcome to The Python Programming"
print(str.endswith("The",4,14))           #since b/w index 4 and index 10, we have "to", hence it is returning true


#find("") method - this method searches for the first occurence of the provided string, if it is present, it returns the index of that word, otherwise -1
n="Prakhar is Prakhar"
print(n.find("Prakhar"))


#isalnum() method - returns true if our string is alphanumeric, otherwisw false
print(n.isalnum())


#isalpha() method - returns true, if the string is only made of alphabets, spaces are also prohibited along with symbols
n="aad "
print(n.isalpha())


#islower() method - returns true, if the string is in lowercase, otherwise false is returned
print(n.islower())


#isprintable() method - returns true if all the charcters is the strings are printsble
s1="Hello World"
print(s1.isprintable())
s1="Hello World\n"
print(s1.isprintable())       #since \n is not printable character, hence false is returned


#isspace() method - returns true only if string contains white spaces
s2=" "
print(s1.isspace())
print(s2.isspace())


#istitle() method - returns true only if the first charcter of each string is in uppercase.
print(s1.istitle())
s2="hello World"
print(s2.istitle())       #false, since h in hello, is not in uppercase 


#swapcase() method - will swap the cases i.e., if a character is in lower case, it will get converted in uppercase and viceversa
print(s1.swapcase())


#title() method - used to convert first charcter of all the strings in uppercase, very useful in real life too!
print(s1.title())


#startswith("argument") - returns true if a string starts with the provided argument
print(s2.startswith("hello"))
