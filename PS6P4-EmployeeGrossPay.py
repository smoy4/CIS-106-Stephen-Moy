# Stephen Moy
# CIS 106 - W01
# 03/01/2024

# Problem Set 6 - Question 4: 

#Input Phase
print("Do you want to use the program that calculates gross pay averages? (Y/N)")
answer = input()
EmployeeCount = 0
GrossPaySum = 0.00
while(answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes"):
  #Process Phase
  print("\nEnter the employee's last name: ")
  lastname = input()
  print("Enter the number of hours worked.")
  hours = float(input())
  print("Enter the hourly pay rate.")
  rate = float(input())
  grosspay = (40 * rate) + ((hours - 40) * (rate * 1.5)) if hours > 40 else hours * rate
  print("Employee: " + lastname)
  print("Gross Pay = $" + str(grosspay))
  EmployeeCount = EmployeeCount + 1
  GrossPaySum = GrossPaySum + grosspay
  print("Do you want to enter another employee? (Y/N)")
  answer = input( )

#Output Phase
print("\nSum of all Gross Pay = $" + str(GrossPaySum))
print("Number of employees: " + str(EmployeeCount))
print("Average Gross Pay = $" + str(GrossPaySum / EmployeeCount))