""" ***** Number Guessing Game ***** """

import random

from numpy import number

#  
a = input("do you want to play the game ? (yes/no) : ")
if a.lower() == "yes":
    print("Great! Let's start the game :")
    print("I have selected a number between 1 and 10. You have 3 attempts to guess it.")
    print(" ")

    choosen_number = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        guess = int(input("Enter your guess (Between 1 and 10) : "))

        if guess < 1 or guess > 10:

            print("Please enter a number between 1 and 10.")
            continue

        if guess == choosen_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess! You have {attempts} attempts left.")
            else:
                print(f"Sorry, you've run out of attempts.\n The correct number was {choosen_number}.")