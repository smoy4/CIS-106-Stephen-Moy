# Stephen Moy
# CIS 106 - W01
# 02/24/2024

# Problem Set 5 - Question 2: Part Number

#Input Phase
print("Please enter the part number: ")
part_number = int(input())
print("How many units of this part are you purchasing? ")
quantity = int(input())

#Process Phase
if part_number == 10 or part_number == 55:
  unit_price = 1.00
elif part_number == 99:
  unit_price = 2.00
elif part_number == 80 or part_number == 70:
  unit_price = 3.00
else:
  unit_price = 5.00

#Output Phase
total_cost = quantity * unit_price
print("\nPart Number: ", part_number)
print("Unit Price: $", unit_price)
print("Total Cost: $", total_cost)