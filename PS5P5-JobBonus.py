# Stephen Moy
# CIS 106 - W01
# 02/24/2024

# Problem Set 5 - Question 5: Job Bonus

#Input Phase
print("Hello Employee! Please enter your last name: ")
lastName = input()
print("Please enter your salary (USD): $")
salary = float(input())
print("Please enter your job level (integer): ")
jobLevel = int(input())

#Process Phase
if jobLevel >= 10:
  bonus = 0.25
elif jobLevel >= 5:
  bonus = 0.20
else:
  bonus = 0.10
BonusAmount = salary * bonus

#Output Phase
print("\nEmployee Last Name: " + lastName)
print("Salary: $" + str(salary))
print("Bonus Amount: $" + str(BonusAmount))