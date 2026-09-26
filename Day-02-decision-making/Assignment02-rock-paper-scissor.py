# rock-paper-scissors game

import random

# display the game title 
print("Rock, paper, scissors Game")
print("**" * 14)

#Get and display the player's choice
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print(f"You chose {player_choice}")

#Generate the computer's choice
computer_choice = random.choice(["rock", "paper", "scissors"])
print(f"Computer chose {computer_choice}")

#Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")