import random
secrete=random.randint(1,20)
print("Welcome to the guessing game")
print("You have 5 attempts to guess the number")
print(secrete)
attempts=0
while attempts<5:
    guess=int(input("Guess a number between 1 and 20: "))
    if guess==secrete:
        print("Your guess is correct")
        break
    elif abs(guess-secrete)<=5:
        if(guess<secrete):
            print("Your guess is close, but low")
        if(guess>secrete):
            print("Your guess is close, but high")
    elif (abs(guess-secrete))>5:
        if(guess<secrete):
            print("Your guess is too low")
        if(guess>secrete):
            print("Your guess is too high")
    if attempts==4:
        print("You have used all your attempts")
        print("The secret number was",secrete)
    attempts+=1
