def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error")
    return a / b

def Modulus(a, b):
    return a % b

def power(a, b):
    return a ** b
print("=======================================================================")
print(" ")
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print(" ")

while True :
    print(" ======= operations on two  numbers ========= ")
    print(" ")
    
    
    print("Enter 1 : addition ")
    print("Enter 2 : subtraction ")
    print("Enter 3 : multiplication ")
    print("Enter 4 : division ")
    print("Enter 5 : remainder")
    print("Enter 6 : power")
    print("Enter 7 : Exit")
    print(" ")

    choice = input("Enter your choice : ")
    

    if choice == "1":
        print("Addition of two numbers = ", add(a, b))

    elif choice == "2":
        print("Subtraction of two number = ", subtraction(a, b))

    elif choice == "3":
            print("Multiplication of two number = ", multiplication(a, b))

    elif choice == "4":
            print("Dvision of two number = ", division(a, b))

    elif choice == "5":
            print("remainder of two number = ", Modulus(a, b))

    elif choice == "6":
            print(f"{a} to the power {b} = ", power(a, b))

    elif choice == "7":
            print("byeee!!!!!!!!!!")
            break


    else:
         print("Invalid choice !!! choose correct one ")