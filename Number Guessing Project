import random

print("Welcome To The Number Guessing Game!")
print("Guess a number between 1 and 100")
choice = random.randint(1, 100)

level = input("Choose a difficulty 'easy' or 'hard': ")
attempts = 0
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Wrong input!")
    exit()

while attempts > 0:

    print(f"You have {attempts} remaining to guess the number!")
    guess = int(input("Make a guess: "))
    if guess > choice:
        attempts -= 1
        print("Too high.")
    elif guess < choice:
        attempts -= 1
        print(f"Too low.")
    else:
        print(f"You got it! The answer was {choice}")
        exit()
    if attempts == 0:
        print(f"Run out of attempts. You lost! The answer was {choice}")
