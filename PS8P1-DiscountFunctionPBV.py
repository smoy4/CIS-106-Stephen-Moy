# Stephen Moy
# CIS 106 - W01
# 03/17/2024

# Problem Set 8 - Problem 1: Extended Price Function

def ComputeExtendedPrice(QTY, UnitPrice):
  ExtendedPrice = QTY * UnitPrice
  DiscountAmount = ExtendedPrice * 0.1 if ExtendedPrice > 10000.0 else 0.0
  ExtendedPrice = ExtendedPrice - DiscountAmount
  return ExtendedPrice

TotalExtendedPrice = 0.0
r = input ("Do you want to compute the extended price? (Yes or No)? ")
while r == "Y" or r == "y":
  QTY = float(input("Enter Quantity: "))
  UnitPrice = float(input("Enter Unit Price: "))
  ExtendedPrice = ComputeExtendedPrice(QTY, UnitPrice)
  TotalExtendedPrice = TotalExtendedPrice + ExtendedPrice
  print("QTY: ", QTY)
  print("Unit Price: ", UnitPrice)
  print("ExtendedPrice is: $", ExtendedPrice)
  print(" ")
  r = input("Do you want to compute the extended price? (Yes or No)? ")
  
print("Total Extended Price is: $", TotalExtendedPrice)
