# my attempt to the higher-lower game
## learns after reviewing solution:
## use function for formatting account data
## logo gets reprinted after clear
## only need one while loop to make game repeatedable vs having a function called game


from random import randint
import os
from higher_lower_art import logo, vs
from higher_lower_game_data import data

def make_random_selection():
    random_value = randint(0, len(data)-1)
    return data[random_value]

def highest_follower_count(selection_A_data, selection_B_data):
    if selection_A_data['follower_count'] >= selection_B_data['follower_count']:
        return selection_A_data['name']
    elif selection_A_data['follower_count'] < selection_B_data['follower_count']:
        return selection_B_data['name']

# def game():
# logo is printed twice
print(logo)
score = 0        
selection_A = make_random_selection()
selection_B = make_random_selection()
game_not_finished = True
    
while game_not_finished:
    print(f"Compare A: {selection_A['name']}, {selection_A['description']}, {selection_A['country']}")
    print(vs)
    # Should have made a function instead of repeating data
    print(f"Against B: {selection_B['name']}, {selection_B['description']}, {selection_B['country']}")
    print(f"***TESTING: follower = {selection_B['follower_count']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == 'A':
        guess = selection_A['name']
    elif guess == 'B':
        guess = selection_B['name']

    answer = highest_follower_count(selection_A, selection_B)
    # clear is needed here and reprint of loogo
    os.system('clear')
    print(logo)

    if guess == answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        # This works as intended
        game_not_finished = False
        print(f"Sorry, that's wrong. Final score: {score}")
    
    selection_A = selection_B
    selection_B = make_random_selection()

# game()


