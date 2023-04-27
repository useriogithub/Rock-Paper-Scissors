import random

user = input("Enter a choice (rock, paper, scissors):")

possible_actions = ["rock", "paper","scissors"]
computer_action = random.choice([possible_actions])

print(f"\nYou chose {user}, computer chose {computer_action}.\n")

#if both players have made their choice, you need to a way to decide who wins. Compare the player's choices and determine a winner:

if user == computer_action:
     print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
     if computer_action == "scissors":
          print("Rock smashes scissors! You win!")
     else:
          print("Paper covers rock! You lose.")
elif user == "paper":
     if computer_action == "rock":
          print("Paper covers rock! You win!")
     else:
          print("Scissor cuts Paper! You lose")
elif user == "scissor":
     if computer_action == "paper":
          print("Scissor cuts paper! You win!")
     else:
          print("Rock smashes scissors! You lose.")