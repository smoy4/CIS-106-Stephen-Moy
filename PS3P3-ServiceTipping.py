# Stephen Moy
# CIS 106 - W01
# 02/09/2024

# Problem Set 3 - Question 3: Service Tipping

#Input Phase
mealTotal = float(input("Enter the total charge for the meal in USD: $"))

#Process Phase
ServiceAverage = mealTotal * 0.15
ServiceGood = mealTotal * 0.18
ServiceExceptional = mealTotal * 0.20

FinalBillAverage = mealTotal + ServiceAverage
FinalBillGood = mealTotal + ServiceGood
FinalBillExceptional = mealTotal + ServiceExceptional

#Output Phase
print("\nAverage Service (15%)")
print("\nMeal Total: $", mealTotal)
print("\nTip Amount: $", round(ServiceAverage,2))
print("\nFinal Bill: $", FinalBillAverage)

print("\n\nGood Service (18%)")
print("\nMeal Total: $", mealTotal)
print("\nTip Amount: $", round(ServiceGood,2))
print("\nFinal Bill: $", FinalBillGood)

print("\n\nExceptional Service (20%)")
print("\nMeal Total: $", mealTotal)
print("\nTip Amount: $", round(ServiceExceptional,2))
print("\nFinal Bill: $", FinalBillExceptional)