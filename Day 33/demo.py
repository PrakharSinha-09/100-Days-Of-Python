dict={"Tony Stark":"Iron Man","Steven Roger":"Captain America","Thor":"God Of Thunder","Dr Banner":"Hulk"}

print(dict)

#Accessing Value wrt to key
print(dict["Tony Stark"])

print(dict.get("Tony Stark"))          #we will get same output for line 6 and 8 but there exist a differnce too and that is..if you are printing line 6, if that key doesn't exist it will throw error while in case of get method, you will get none

print(dict.keys())                     #this will return all the keys of the dictionary.

#Via Iteration
# for item in dict:
#     print(item,":",dict[item]) 

#Getting Keys Via Iteration
for key in dict.keys():
    print("The Value Corresponding to ",key,"is ",dict[key]) 

print(dict.items())    #this Will return key, value packed in tuple

for key,value in dict.items():
    print(key,":",value)