# Stephen Moy
# CIS 106 - W01
# 02/18/2024

# Problem Set 4 - Question 3: Book Order Shipping

#Input Phase
print("How many books are you ordering? Enter an integer value: ")
BookQTY = int(input())
print("How much does each book cost? Enter a decimal value in USD: ")
BookUnitPrice = float(input())

#Process Phase
Subtotal = round(BookQTY * BookUnitPrice,2)
if Subtotal == 0:
  print("Your cart is empty!")
  Shipping = 0
elif Subtotal > 50:
  print("You qualify for free shipping by exceeding $50 in books!")
  Shipping = 0
else:
  print("A shipping charge of $25.00 will be applied to your order.")
  Shipping = 25.00
Total = Subtotal + Shipping
#Output Phase
print("\nYour order subtotal is: $" + str(Subtotal))
print("Your shipping charge is: $" + str(Shipping))
print("Your total order cost is: $" + str(Total))