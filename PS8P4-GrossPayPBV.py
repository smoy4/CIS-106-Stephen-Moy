# Stephen Moy
# CIS 106 - W01
# 03/17/2024

# Problem Set 8 - Problem 4: Gross Pay Function PBV

def ComputePayRate(JobCode):
  if JobCode == "L":
    PayRate = 25
  elif JobCode == "A":
    PayRate = 30
  elif JobCode == "J":
    PayRate = 50
  return PayRate
  
TotalGrossPays = 0.0
r = input("Do you want to compute an employee's gross pay? (Y/N) ")
while r == "Y" or r == "y":
  EmployeeLastName = input(str("Enter Employee Last Name: "))
  HoursWorked = float(input("Enter Hours Worked: "))
  PayRate = ComputePayRate(input("Enter Job Code: "))
  GrossPay = HoursWorked * PayRate
  print("Emloyee Last Name: ", EmployeeLastName)
  print("Employee Gross Pay: $", GrossPay)
  print(" ")
  TotalGrossPays = TotalGrossPays + GrossPay
  r = input("Do you want to compute another employee's gross pay? (Y/N) ")

print("Total Gross Pays: $", TotalGrossPays)
