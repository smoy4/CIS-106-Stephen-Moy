# Stephen Moy
# CIS 106 - W01
# 03/21/2024

# Problem Set 9 - Problem 3: Car Shopping

def CalculateDiscount(Make, Model, EVCode, MSRP):
  if (EVCode == "Y"):
    Discount = 0.30
  elif (Make == "Toyota" and Model == "Rav4" and EVCode == "N"):
    Discount = 0.15
  elif (Make == "Honda" and Model == "Accord" and EVCode == "N"):
    Discount = 0.10
  else:
    Discount = 0.05
  DiscountedPrice = MSRP - (MSRP * Discount)
  SalesPrice = DiscountedPrice * 1.07
  return SalesPrice

TotalMSRPPrice = 0.0
TotalSalesPrice = 0.0
r = input ("Do you want to compute the MSRP of a car? (Yes or No)? ")
while r == "Y" or r == "y":
  Make = input ("Enter the make of the car: ")
  Model = input ("Enter the model of the car: ")
  EVCode = input ("Enter the EV code of the car (Y or N): ")
  MSRP = float(input ("Enter the base price of the car: $"))
  TotalMSRPPrice = TotalMSRPPrice + MSRP
  SalesPrice = CalculateDiscount (Make, Model, EVCode, MSRP)
  print ("The Sales Price of the car is: $", format(SalesPrice, ',.2f'))
  TotalSalesPrice = TotalSalesPrice + SalesPrice
  print(" ")
  r = input ("Do you want to compute the MSRP of a car? (Yes or No)? ")

print("The sum of all the MSRP prices is: $", format(TotalMSRPPrice,',.2f'))
print("The sum of all the Sales Prices is: $", format(TotalSalesPrice,',.2f'))