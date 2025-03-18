import random

# Define choices
choices = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Validate input
if user_choice not in choices:
    print("Invalid choice!")
    exit()

# Get computer choice
computer_choice = random.choice(choices)

# Determine the winner
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")