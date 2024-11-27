


import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling App!")
    while True:
        user_input = input("Press 'r' to roll the dice or 'q' to quit: ").lower()
        if user_input == 'r':
            print(f"You rolled a {roll_dice()}!")
        elif user_input == 'q':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please press 'r' to roll or 'q' to quit.")

if __name__ == "__main__":
    main()
