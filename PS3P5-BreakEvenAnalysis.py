# Stephen Moy
# CIS 106 - W01
# 02/08/2024

# Problem Set 3 - Question 5: Break-Even Analysis

#Input Phase
CostsFixed = float(input("Enter the fixed costs: "))
UnitPrice = float(input("Enter the unit price: "))
UnitCost = float(input("Enter the unit cost: "))

#Processing Phase
BreakEvenPoint = CostsFixed / (UnitPrice - UnitCost)

#Output Phase
print("The break-even point is: ", BreakEvenPoint, " minimum units you need to sell ")
print("in order to keep your business afloat.")