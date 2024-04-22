# Stephen Moy
# CIS 106 - W01
# 04/20/2024

# Problem Set 13 - Problems 1: Employee Class

class Employee:
  def __init__(self, first, last, salary, startdate):
    self.first = first
    self.last = last
    self.salary = salary
    self.startdate = startdate
    self.email = first[0] + last + "@dbsterlin.com"

  def bonus(self, rate):
    b = float(rate) * float(self.salary)
    return b

employee374 = Employee("Stephen", "Moy", 101961.60, "09/19/2022")

print("First Name: " + employee374.first)
print("\nLast Name: \t" + employee374.last)
print("\nEmail: \t\t" + employee374.email)
print("\nStart Date: " + employee374.startdate)
print("\nSalary: \t$" + format(employee374.salary, '.2f'))
print("\n10% Bonus: \t$" + format(employee374.bonus(0.10), '.2f'))
print("\n20% Bonus: \t$" + format(employee374.bonus(0.20), '.2f'))