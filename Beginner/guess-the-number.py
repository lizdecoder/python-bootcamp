import random
import os
from guess_the_number_art import logo

def check_guess(guess, answer):
    if guess > answer:
        return f"Too high."
    elif guess < answer:
        return f"Too low."

def play_game():
    print(logo)
    
    is_game_over = False
    answer = random.randrange(1,100,1)
    level = {
        "easy": 10,
        "hard": 5,
    }
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"*****FOR TESTING ONLY: The correct answer is {answer}*****")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy' or difficulty == 'hard':
        attempts = level[difficulty]
        
        while not is_game_over:
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
            attempts -= 1

            if user_guess == answer:
                print(f"You got it! The answer is {answer}")
                is_game_over = True
            elif attempts == 0:
                print(f"You've run out of guesses, you lose.")
                is_game_over = True
            else:
                print(check_guess(guess=user_guess, answer=answer))
                print("Guess again.")
    else:
        print("You have entered an invalid response.")

play_game()

while input("\nDo you want to play again? Type 'y' or 'n': ").lower() == "y":
    os.system('clear')
    play_game()