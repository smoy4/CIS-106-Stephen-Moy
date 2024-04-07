# Stephen Moy
# CIS 106 - W01
# 04/04/2024

# Problem Set 10 - Problem 5: Tax Global Variable

def computeTotal(quantity, price):
  global total
  total = quantity * price
  global tax
  tax = total * 0.07
  return

total = 0.0
tax = 0.0
quantity = float(input("Enter the item quantity: "))
price = float(input("Enter the item price : $"))
computeTotal(quantity, price)
print("\nThe total is $", format(float(total), '.2f'))
print("The tax is $", format(float(tax), '.2f'))