""" Local variables """

""" def calculate_total(price, tax):
    total = price + tax     # `total` is local to this function
    return total

calculate_total(10, 2)
print(total)                # NameError: name 'total' is not defined """


""" Global variables """

message = "Hello"

def greet():
    print(message)   # Reading a global variable is fine

greet()              # Output: Hello
print(" ")


color = "blue"

def change_color():
    color = "red"   # This creates a new local variable, not the global one

change_color()
print(color)        # Output: blue
print(" ")

""" The global keyword (use sparingly) """

count = 0

def increment():
    global count
    count = count + 1

increment()
print(count)   # Output: 1
print(" ")


def increment(count):
    return count + 1

count = 0
count = increment(count)
print(count)   # Output: 1
print("  ")

