import os
from secret_auction_art import logo
#HINT: You can call clear() to clear the output in the console.
# can use to visualize code: https://pythontutor.com/visualize.html#mode=edit

print(logo)

bids = {}
other_bidders = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid

    others = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if others == 'yes':
        os.system('clear')
    elif others == 'no':
        other_bidders = True
        find_highest_bidder(bids)

        # first attempt
        # highest_value = 0
        # for key in bids:
        #     value = int(bids[key])
        #     if highest_value < value:
        #         highest_value = value
        #         bidder = key
        # print(f"The winner is {bidder} with a bid of ${highest_value}.")