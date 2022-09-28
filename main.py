from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def highest_bidder_cal(bidding_record):
    highest_bidder = 0
    winner = ""
    winner_02 = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bidder}")

while not bidding_finished:
    name = input("What's your name?: ")
    price = int(input("What's your bid?:$ "))
    bids[name] = price
    more_bidders = input("Are there any more bidders? Type 'Yes' or 'No' ").lower()
    if more_bidders == "no":
        bidding_finished = True
        highest_bidder_cal(bids)
    elif more_bidders == "yes":
        clear()
