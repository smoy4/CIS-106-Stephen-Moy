# Stephen Moy
# CIS 106 - W01
# 02/24/2024

# Problem Set 5 - Question 3: CD - First Year Investment

#Input Phase
print("Enter the initial investment amount (principal) in USD: $")
principal = float(input())
print("Enter desired term length in years: ")
term = int(input())

#Process Phase
if principal > 100000 and term == 5:
    interest_rate = 0.06
elif principal >= 50000 and principal <= 100000 and term == 10:
    interest_rate = 0.05
elif principal >= 50000 and principal <= 100000 and term == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
FirstYearInvestment = round(principal * (1 + interest_rate),2)

#Output Phase
print("\nThe principal investment amount is: $", principal)
print("The interest rate is: ", interest_rate)
print("The first year investment amount is: $", FirstYearInvestment)