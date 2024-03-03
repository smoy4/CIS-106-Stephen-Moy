# Stephen Moy
# CIS 106 - W01
# 03/01/2024

# Problem Set 6 - Question 5: Cumulative Discount Orders

#Input Phase
print("Do you want to run this program that calculates the cumulative discount orders?")
print("Enter Y for Yes or N for No")
answer = input()
CumulativeDiscount = 0
NumberOfOrders = 0

while(answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes"):
  #Process Phase
  print("\nEnter the number of items ordered: ")
  items = int(input())
  print("Enter the price of each item in USD: ")
  price = float(input())
  ExtendedPrice = items * price
  if(ExtendedPrice > 10000):
    DiscountAmount = ExtendedPrice * 0.25
  else:
    DiscountAmount = ExtendedPrice * 0.10
  TotalOrderPrice = ExtendedPrice - DiscountAmount
  CumulativeDiscount = CumulativeDiscount + DiscountAmount
  NumberOfOrders = NumberOfOrders + 1
  print("The extended price is: $", ExtendedPrice)
  print("Discount Earned: $", DiscountAmount)
  print("The total order price is: $", TotalOrderPrice)
  print("Do you want to enter another order? (Y/N)")
  answer = input()

#Output Phase
print("\nThe cumulative discount amount is: $", CumulativeDiscount)
print("The total number of orders is: ", NumberOfOrders)
print("The average discount amount is: $", CumulativeDiscount/NumberOfOrders)