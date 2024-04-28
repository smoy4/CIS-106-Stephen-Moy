# Stephen Moy
# CIS 106 - W01
# 04/24/2024

# Problem Set 14 - Problems 1: Employee/Manager Class/Object/Inheritance

class Employee:
  rate = 0.10
  def __init__(self, first, last, salary, startdate):
    self.first = first
    self.last = last
    self.salary = salary
    self.startdate = startdate
    self.email = first[0] + last + "@dbsterlin.com"

  def applybonus(self):
    self.salary = self.salary * self.rate

class Manager(Employee):
  rate = 0.20
  def __init__(self, first, last, salary, startdate):
    super().__init__(first, last, salary, startdate)
    self.longtermbonus = self.salary * 0.40

employee374 = Employee("Stephen", "Moy", 101961.60, "09/19/2022")
manager001 = Manager("Regine", "Jeune", 250000.00, "06/15/2003")

print("First Name: " + employee374.first)
print("Last Name: \t" + employee374.last)
print("Email: \t\t" + employee374.email)
print("Start Date: " + employee374.startdate)
print("Salary: \t$" + format(employee374.salary, '.2f'))
employee374.applybonus()
print("Bonus: \t\t$" + format(employee374.salary, '.2f'))

print("\n\nFirst Name: " + manager001.first)
print("Last Name: \t" + manager001.last)
print("Email: \t\t" + manager001.email)
print("Start Date: " + manager001.startdate)
print("Salary: \t$" + format(manager001.salary, '.2f'))
manager001.applybonus()
print("Bonus: \t\t$" + format(manager001.salary, '.2f'))
print("Longterm Bonus: $" + format(manager001.longtermbonus, '.2f'))