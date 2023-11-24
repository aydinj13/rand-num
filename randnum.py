import random

# Features to add: try...except if users don't enter yes/no for hearts prompt


def guess_x(include_hearts):
    while True:
        y = int(input("Numbers Possible: "))
        if y >= 5:
            randInt = random.randint(0, y)
            break
        else:
            print("Amount of Numbers should at least be 5.")

    if include_hearts:
        hearts = round(y / 5)
        print(f"Guess x between 0 and {y}! You have {hearts} hearts!")
    else:
        hearts = None

    while hearts is None or hearts > 0:
        x = int(input("Guess a number: "))

        if x > randInt:
            print(f"Lower than {x}")
        elif x < randInt:
            print(f"Higher than {x}")
        else:
            print("Correct!")
            break

        if include_hearts:
            hearts -= 1
            print(f"Hearts: {hearts}")

    if hearts == 0 and include_hearts:
        print("Game Over.")

# Ask the user whether they want hearts or not
while True:
    user_choice = input("Do you want hearts in the game? (yes/no): ").lower()
    if user_choice in ['yes', 'no']:
        break
    else:
        print("Please enter 'yes' or 'no'.")

include_hearts = True if user_choice == 'yes' else False

# Run the game based on user's choice
guess_x(include_hearts)