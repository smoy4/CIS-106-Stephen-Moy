# Stephen Moy
# CIS 106 - W01
# 04/04/2024

# Problem Set 10 - Problem 1: Discount Amount

def compute_discount(quantity, price, discountRate):
  extendedprice = quantity * price
  discountAmount = extendedprice * discountRate
  discountedPrice = extendedprice - discountAmount
  return discountAmount, discountedPrice

quantity = int(input("Enter the quantity of the item: "))
price = float(input("Enter the price of the item: $"))
discountRate = float(input("Enter the discount rate (in decimal, 0.1 = 10%): "))
discountAmount, discountedPrice = compute_discount (quantity, price, discountRate)

print("\nQuantity: ", quantity)
print("Price: $", format(price, '0.2f'))
print("Discount Amount: $", format(discountAmount, '0.2f'))
print("Discounted Price: $", format(discountedPrice, '0.2f'))