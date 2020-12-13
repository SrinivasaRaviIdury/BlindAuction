#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
import os
clear = lambda: os.system('cls')
bidding = []
new_bidder = "yes"
while new_bidder == "yes":
    add_bidder={}
    name=input('what is your name :').lower()
    amount= round(float(input('enter your bid amount $')),2)
    add_bidder['name'] = name
    add_bidder['amount'] = amount
    bidding.append(add_bidder)
    new_bidder = input("Is any one there for bidding if yes else no: ").lower()
    clear()

bidder_name =""
highest_bid = 0
for i in bidding:
    if i['amount']>highest_bid:
        bidder_name = i['name']
        highest_bid = i['amount']
print(f"Person won the bid is: {bidder_name}, and amount is {highest_bid}")







