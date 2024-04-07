# Stephen Moy
# CIS 106 - W01
# 04/04/2024

# Problem Set 10 - Problem 3: Sales Commission

def salesForecast(salesamount):
  CommissionRate = 0.0
  if salesamount > 100000:
    CommissionRate = 0.10
  elif salesamount <= 100000:
    CommissionRate = 0.05
  Commission = salesamount * CommissionRate
  nextyearSales = salesamount * 1.05
  return Commission, nextyearSales

employeelastname = input("Enter employee's last name: ")
salesamount = float(input("Enter this year's sales amount: $"))
Commission, nextyearSales = salesForecast (salesamount)
print("\nEmployee's last name: ", employeelastname)
print("Commission: $", format(Commission, ',.2f'))
print("Next year's sales target: $", format(nextyearSales, ',.2f'))