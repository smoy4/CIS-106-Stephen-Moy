# Stephen Moy
# CIS 106 - W01
# 02/18/2024

# Problem Set 4 - Question 2: Check Item A or B

#Input Phase
print("Instructions: Enter 'A' for Item A. Enter anything else for Item B.")
print("Which item do you want to check?")
ItemChoice = input()
print("How many units do you want to buy? Enter an integer: ")
ItemQTY = int(input())

#Process Phase
if ItemChoice == "A":
  print("\nYou chose Item A, which is $10 / unit.")
  UnitPrice = 10
else:
  print("\nYou chose Item B, which is $20 / unit.")
  UnitPrice = 20
ExtendedPrice = UnitPrice * ItemQTY

#Output Phase
print("Item Quantity: " + str(ItemQTY) + " units.")
print("Extended Price: $" + str(ExtendedPrice))