""" Multiplication Table """

inter = int(input("Enter a number to generate its multiplication table: "))

for i in range (1, 11):
    result = inter * i
    print(f"{inter} x {i} = {result}")