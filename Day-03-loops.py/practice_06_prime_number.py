""" Check if a Number is Prime """

inter = int(input("Enter a number to check if it is prime: "))

if inter % 2 == 0 and inter > 2:
    print(f"{inter} is not a prime number.")
else:
    print(f"{inter} is a prime number.")