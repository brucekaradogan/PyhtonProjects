import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game_elements = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

if 0 <= user_choice <= 2:
    print(f"Your choice:{game_elements[user_choice]}")
    print(f"Computer choice:{game_elements[computer_choice]}")
    if computer_choice == user_choice:
        print("It's a draw!")
    elif computer_choice == 2 and user_choice == 0:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
else:
    print("Enter a valid input to play the game!")
