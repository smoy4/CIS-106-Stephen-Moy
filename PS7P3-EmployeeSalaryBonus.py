# Stephen Moy
# CIS 106 - W01
# 03/08/2024

# Problem Set 7 - Question 3:
f = open("dataPS7P3.txt", "r")

#Input Phase
TotalBonus = 0
c = 0

#Process Phase
LastName = str(f.readline().rstrip('\n'))
while LastName != "":
  Salary = float(f.readline())
  if Salary >= 100000:
    BonusRate = 0.20
  elif Salary >= 50000:
    BonusRate = 0.15
  else:
    BonusRate = 0.10
  Bonus = Salary * BonusRate
  TotalBonus = TotalBonus + Bonus
  c = c + 1
  print("Employee Last Name: ", LastName)
  print("Employee Salary: $", format(Salary, ',.2f'))
  print("Employee Bonus: $", format(Bonus, ',.2f'))
  print(" ")
  LastName = str(f.readline().rstrip('\n'))

#Output Phase
f.close()
AverageBonus = TotalBonus / c
print("Number of Employees: ", c)
print("Total Bonuses: $", format(TotalBonus, ',.2f'))
print("Average Bonus: $", format(AverageBonus, ',.2f'))
