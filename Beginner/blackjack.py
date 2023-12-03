############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
import os
from blackjack_art import logo

def deal_card(num_of_cards):
    return random.choices(cards, k=num_of_cards)

def calculate_score(cards):
    score = sum(cards)
    if len(cards) == 2: 
        if score == 21:
            score = 0
        elif score > 21:
            cards.remove(11)
            cards.append(1)
            score = calculate_score(cards)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("draw")
    elif computer_score == 0 or user_score > 21:
        print("you lose")
    elif user_score == 0 or computer_score > 21:
        print("you win")
    else:
        if user_score > computer_score:
            print("else: you win")
        else:
            print("else: you lose")
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    game_continues = True
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    print(logo)

    if game == 'y':
        user_cards = []
        computer_cards = []
        user_cards = deal_card(2)
        computer_cards = deal_card(2)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}, [[[[hidden card: {computer_cards[1]}]]], current score: {computer_score}.")
        
        while game_continues:

            if user_score == 0 or computer_score == 0 or user_score > 21:
                print("inside if blackjack statement")
                game_continues = False
                compare(user_score, computer_score)
            
            else:
                draw_again = input("Do you want to draw another card. Type 'y' for yes and 'n' for no.: ").lower()
                
                if draw_again == 'y':
                    another_card = deal_card(1)
                    user_cards.extend(another_card)
                    user_score = calculate_score(user_cards)
                    print(f"Made it in if another_card, new card is: {another_card} with cards of {user_cards}, new score: {user_score}")
                    print(f"In another_card, Computer cards now: {computer_cards}, with computer score: {computer_score}")
                elif draw_again == 'n':
                    if computer_score < 17:
                        computer_cards.extend(deal_card(1))
                        computer_score = calculate_score(computer_cards)   
                        print("'n' draw again: made it in else if statement") 
                
                    game_continues = False     
                    print(f"Your final hand: {user_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    compare(user_score, computer_score)

        play_again = input("Do you wish to play again. Type 'y' for yes and 'n' for no.: ").lower()
        if play_again == 'y':
            os.system('clear')
            blackjack()
        elif play_again == 'n':
            print("Thank you for playing. The end.")
    else:        
        print("You chose not to play Blackjack.")

blackjack()
            