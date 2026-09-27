""" Count the Number of Digits in a Number """

inter = int(input("Enter a number to count its digits: "))
count = 0
temp = inter  # Store the original number for display

while temp != 0:
    temp //= 10
    count += 1

print(f"The number of digits in {inter} is {count}.")