import random

# Generate a random secret number between 1 and 20
secrete = random.randint(1, 20)

# Print welcome messages and instructions
print("Welcome to the guessing game")
print("You have 5 attempts to guess the number")

# Initialize the number of attempts
attempts = 0

# Loop until the user has used all attempts or guesses correctly
while attempts < 5:
    # Prompt the user to guess a number
    guess = int(input("Guess a number between 1 and 20: "))

    # Check if the guess is correct
    if guess == secrete:
        print("Your guess is correct")
        break  # Exit the loop if the guess is correct

    # Check if the guess is close (within 5) to the secret number
    elif abs(guess - secrete) <= 5:
        if guess < secrete:
            print("Your guess is close, but low")
        if guess > secrete:
            print("Your guess is close, but high")

    # Check if the guess is far (greater than 5) from the secret number
    elif abs(guess - secrete) > 5:
        if guess < secrete:
            print("Your guess is too low")
        if guess > secrete:
            print("Your guess is too high")

    # If this is the last attempt, inform the user and reveal the secret number
    if attempts == 4:
        print("You have used all your attempts")
        print("The secret number was", secrete)

    # Increment the number of attempts
    attempts += 1
