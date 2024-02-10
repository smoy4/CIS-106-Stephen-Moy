# Stephen Moy
# CIS 106 - W01
# 02/09/2024

# Problem Set 3 - Question 2: Stock Investment 2

#Input Phase
print("Please input stock current price and stock purchase price in WHOLE USD.")
print("\nWhat was the purchase price of the stock in USD?")
StockPurchasePrice = float(input("Enter Stock Purchase Price: $"))
print("\nWhat is the current stock worth in USD?")
StockCurrentPrice = float(input("Enter Stock Current Price: $"))


print ("\nHow many Shares do you want to buy? Input must be in whole numbers.")
ShareNumber = int(input("Enter Number of Shares: "))

#Process Phase
StockPortfolioValue = round((StockCurrentPrice - StockPurchasePrice) * ShareNumber,2)

#Output Phase
if StockPortfolioValue > 0: 
  print("\nCongratulations! By investing in this stock,")
  print("you made a profit of $",StockPortfolioValue,"USD.")
elif StockPortfolioValue == 0: 
  print("\nYour investments have not made any money yet.")
  print("Keep your money invested longer to see what happens!")
else:
  print("\nOh no! Your portfolio value is: $",StockPortfolioValue)
  print("Your investments have lost money, but this could be a golden")
  print("opportunity to buy more as the stock will most likely rebound!")