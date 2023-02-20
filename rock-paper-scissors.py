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

game_images = [rock, paper, scissors]
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if choice >=3 or choice < 0:
    print("You typed an invalide number, you lose!")
else:
    print(game_images[choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose: \n" + game_images[computer_choice])

# if choice == 0:
#     print(rock + "\nComputer chose:\n")
#     if computer_choice == 0:
#         print(f'{rock} \nDraw')
#     elif computer_choice == 1:
#         print(f'{paper} \nYou lose')
#     else:
#         print(f'{scissors} \nYou win')
# elif choice == 1:
#     print(paper + "\n Computer chose:\n")
#     if computer_choice == 0:
#         print(f'{rock} \n You win')
#     elif computer_choice == 1:
#         print(f'{paper} \nDraw')
#     else:
#         print(f'{scissors} \nYou lose')
# else:
#     print(scissors + "\n Computer chose:\n")
#     if computer_choice == 0:
#         print(f'{rock} \n You lose')
#     elif computer_choice == 1:
#         print(f'{paper} \nYou win')
#     else:
#         print(f'{scissors} \nDraw')

# refactored
    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and choice == 2:
        print("You lose")
    elif computer_choice > choice:
        print("You lose")
    elif choice > computer_choice:
        print("You win")
    elif computer_choice == choice:
        print("It's a draw")




