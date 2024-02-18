# Stephen Moy
# CIS 106 - W01
# 02/18/2024

# Problem Set 4 - Question 5: Taxes and Dependents

#Input Phase
print("Enter the your last name: ")
LastName = input()
print("What is your gross income? Enter Gross Income in USD: $")
GrossIncome = float(input())
print("How many dependents are you claiming? Enter Dependents (integer): ")
NumberDependents = int(input())

#Process Phase
AdjustedGrossIncome = GrossIncome - (NumberDependents * 12000)
if AdjustedGrossIncome > 50000:
  TaxRate = 0.20
  IncomeTax = AdjustedGrossIncome * TaxRate
elif AdjustedGrossIncome > 0:
  TaxRate = 0.10
  IncomeTax = AdjustedGrossIncome * TaxRate
else:
  TaxRate = 0
  IncomeTax = 100
  print("Super broke people still need to contribute something to society!")

#Output Phase
print("\nLast Name: ", LastName)
print("Gross Income: $", GrossIncome)
print("Number of Dependents: ", NumberDependents)
print("Adjusted Gross Income: $", AdjustedGrossIncome)
print("Income Tax: $", IncomeTax)