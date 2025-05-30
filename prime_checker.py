# Checks whether a given number is prime, composite, or invalid using efficient logic and user input.
import math


def check_prime(number):
    if number < 1:
        print(f"{number} is not a valid input (must be ≥ 1).")
    elif number == 1:
        print("1 is neither Prime nor Composite.")
    elif number == 2:
        print("2 is Prime!")
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                print(f"{number} is Composite: {i} × {number // i} = {number}")
                break
        else:
            print(f"{number} is Prime!")


while True:
    try:
        user_input = int(input("Enter a number (0 to exit): "))
        if user_input == 0:
            print("You exited!")
            break
        check_prime(user_input)
    except ValueError:
        print("Please enter a valid integer.")
