""" Factorial """

inter = int(input("Enter a number to calculate its factorial: "))

factorial = 1

for i in range (1, inter + 1):
    factorial *= i

print(f"The factorial of {inter} is {factorial}.")