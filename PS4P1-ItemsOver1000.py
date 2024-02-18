# Stephen Moy
# CIS 106 - W01
# 02/18/2024

# Problem Set 4 - Question 1: Buying in Bulk

#Input Phase
ItemQuantity = int(input("Enter the number of items you are purchasing: "))

#Process Phase
if ItemQuantity >= 1000:
  UnitPrice = 3.00
else: 
  UnitPrice = 5.00
ExtendedPrice = ItemQuantity * UnitPrice
Tax = round(ExtendedPrice * 0.07,2)
TotalPrice = ExtendedPrice + Tax
#Output Phase
print("\nItem Quantity: ", ItemQuantity, "units")
print("Unit Price: $", UnitPrice, "/ unit")
print("Extended Price: $", ExtendedPrice)
print("Sales Tax: $", Tax)
print("Total Price: $", TotalPrice)