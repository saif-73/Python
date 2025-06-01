# A simple Rock-Paper-Scissors game where the user plays against the computer.
import random

roshambo = ("rock", "paper", "scissors")
computer_side = random.choice(roshambo)
user_side = input("Enter your choice (rock, paper or scissors): ").lower()

if user_side not in roshambo:
    print("Invalid input! Please enter rock, paper, or scissors.")
elif user_side == computer_side:
    print(
        f"\nYou--->{user_side.upper()}\tComputer--->{computer_side.upper()}\n\tMatch is draw!"
    )
elif user_side == "scissors" and computer_side == "paper":
    print(
        f"\nYou--->{user_side.upper()}\tComputer--->{computer_side.upper()}\n\tYou Win!"
    )
elif user_side == "paper" and computer_side == "scissors":
    print(
        f"\nYou--->{user_side.upper()}\tComputer--->{computer_side.upper()}\n\tComputer Wins!"
    )
elif user_side == "rock" and computer_side == "scissors":
    print(
        f"\nYou--->{user_side.upper()}\tComputer--->{computer_side.upper()}\n\tYou Win!"
    )
elif user_side == "scissors" and computer_side == "rock":
    print(
        f"\nYou--->{user_side.upper()}\tComputer--->{computer_side.upper()}\n\tComputer Wins!"
    )
elif user_side == "paper" and computer_side == "rock":
    print(
        f"\nYou--->{user_side.upper()}\tComputer--->{computer_side.upper()}\n\tYou Win!"
    )
elif user_side == "rock" and computer_side == "paper":
    print(
        f"\nYou--->{user_side.upper()}\tComputer--->{computer_side.upper()}\n\tComputer Wins!"
    )
