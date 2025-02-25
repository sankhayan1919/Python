def winner(bidder_data):
  winner=""
  highest_bid=0
  for bidder, bid in bidder_data.items():
    if bid > highest_bid:
      highest_bid=bid
      winner=bidder
  print(f"The list of bidders is: ")
  for bidder in bidder_data.keys():
    print(bidder)
  print(f"The winner is: {winner} with a bid of {highest_bid}")
auction_data={}
end=False
while not end:
  name=input("Enter the name:")
  bid=int(input("Enter the bid:"))
  auction_data[name]=bid
  more_bidders=input("Enter 'yes' or 'no':")
  if more_bidders=='no':
    end=True
    winner(auction_data)