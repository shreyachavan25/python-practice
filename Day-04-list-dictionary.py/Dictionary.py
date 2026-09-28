""" Dicti0nary """

user = {"name": "Alex", "age": "25", "email": "alex@example.com" }
print(user)
print(user["name"]) #output : Alex
print(user["age"])  # output : 25

print(user.get("phone")) #output : None
print(user.get("phone", "not listed")) # output : not listed 
print(" ")



""" OPERATIONS ON DICTIONARY """

user["city"] = "pune"  # Add a new key
print(user)
user["age"] = 26  #update the existing key
print(user)
del user ["age"] # Remove a key
print(user)
print("name" in user)
city = user.pop("city")
print(city)
print()



""" ITERATING OVER A DICTIONARY """

user = {"name": "Alex", "age": "25", "email": "alex@example.com" }

for key, values in user.items():
    print(f"{key} : {values}")      
