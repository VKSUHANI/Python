# Password Generator
# This program generates a random password of a specified length.
# It includes uppercase letters, lowercase letters, digits, and special characters.

import random  # Importing the random module for generating random choices
import string  # Importing the string module for character sets

def password_generator(length):
    # Define character sets for the password
    char = string.ascii_letters  # Uppercase and lowercase letters
    digits = string.digits       # Digits 0-9
    special = string.punctuation # Special characters like @, #, $, etc.
    password_string = [random.choice(char), random.choice(digits), random.choice(special)]  # Ensure at least one character from each set
    # Generate a random selection of characters, digits, and special characters
    password = random.choices(char + digits + special, k=length-3) + password_string
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert the list of characters into a string
    password = ''.join(password)
    
    return password  # Return the generated password

# Prompt the user to enter the desired password length
password = password_generator(int(input("Enter the length of the password: ")))

# Print the generated password
print(password)