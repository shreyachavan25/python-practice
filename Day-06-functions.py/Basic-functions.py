""" Defining a function """

def greet():
    print("Hello, world!")

greet()   # Output: Hello, world!
print(" ")

""" Adding parameters """

def greet(name):
    print(f"Hello, {name}!")

greet("Alex")     # Output: Hello, Alex!
greet("Sam")      # Output: Hello, Sam!
print(" ")

# multiple parameters 

def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alex", "Hi")   # Output: Hi, Alex!
print(" ")

""" Default parameter values """

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alex")             # Output: Hello, Alex!
greet("Alex", "Welcome")  # Output: Welcome, Alex!
print(" ")


""" Keyword arguments """

greet(name="Alex", greeting="Welcome")