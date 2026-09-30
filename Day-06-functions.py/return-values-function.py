""" Returning a value """

def add(a, b):
    return a + b

result = add(3, 4)
print(result)   # Output: 7
print(" ")

""" Returning multiple values """

#coordinates example
def get_coordinates():
    return 10.0, 20.0

x, y = get_coordinates()
print(f"x: {x}, y: {y}")   # Output: x: 10.0, y: 20.0
print(" ")

""" Functions with no return value """

def greet(name):
    print(f"Hello, {name}!")

result = greet("Alex")
print(result)   # Output: None
print(" ")