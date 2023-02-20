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

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

computer_choice = random.randint(0, 2)

if choice == 0:
    print(rock + "\nComputer chose:\n")
    if computer_choice == 0:
        print(f'{rock} \nDraw')
    elif computer_choice == 1:
        print(f'{paper} \nYou lose')
    else:
        print(f'{scissors} \nYou win')
elif choice == 1:
    print(paper + "\n Computer chose:\n")
    if computer_choice == 0:
        print(f'{rock} \n You win')
    elif computer_choice == 1:
        print(f'{paper} \nDraw')
    else:
        print(f'{scissors} \nYou lose')
else:
    print(scissors + "\n Computer chose:\n")
    if computer_choice == 0:
        print(f'{rock} \n You lose')
    elif computer_choice == 1:
        print(f'{paper} \nYou win')
    else:
        print(f'{scissors} \nDraw')




