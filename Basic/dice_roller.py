import random

def roll_dice():
    random_number = random.randint(1, 6)  # Generate a random number between 1 and 6
    return random_number  # Return the generated number

roll_dice()  # Call the function to roll the dice
print(f"Dice rolled: {roll_dice()}")  # Print the result of the dice roll