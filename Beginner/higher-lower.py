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

def game():
    score = 0        
    selection_A = make_random_selection()
    selection_B = make_random_selection()
    game_not_finished = True
    
    while game_not_finished:
        # TODO: must determine proper location of logo
        print(logo)
        print(f"Compare A: {selection_A['name']}, {selection_A['description']}, {selection_A['country']}")
        print(f"***TESTING: follower = {selection_A['follower_count']}")
        print(vs)
        print(f"Against B: {selection_B['name']}, {selection_B['description']}, {selection_B['country']}")
        print(f"***TESTING: follower = {selection_B['follower_count']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess == 'A':
            guess = selection_A['name']
        elif guess == 'B':
            guess = selection_B['name']

        answer = highest_follower_count(selection_A, selection_B)
        print(f"***TESTING guess is: {guess} and answer is: {answer}")
        # TODO: need to make code more efficient, without clear, there's double information
        # os.system('clear')

        if guess == answer:
            score += 1
            # TODO: must determine proper location of logo; duplicate now
            # print(logo)
            print(f"You're right! Current score: {score}")
        else:
            # This works as intended
            game_not_finished = False
            # TODO: must determine proper location of logo; this is technically right, but it's due to clear screen
            # print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
        
        selection_A = selection_B
        selection_B = make_random_selection()

game()


