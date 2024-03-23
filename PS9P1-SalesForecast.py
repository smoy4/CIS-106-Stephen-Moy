# Stephen Moy
# CIS 106 - W01
# 03/21/2024

# Problem Set 9 - Problem 1: Sales Forecast

def ComputeSalesForecast(SalesCurrentMonth, CurrentMonth):
  if (CurrentMonth == "December" or 
      CurrentMonth == "January" or 
      CurrentMonth == "February"):
    SalesNextMonth = SalesCurrentMonth * 1.10
    return SalesNextMonth
  elif (CurrentMonth == "March" or 
        CurrentMonth == "April" or 
        CurrentMonth == "May"):
    SalesNextMonth = SalesCurrentMonth * 1.15
    return SalesNextMonth
  elif (CurrentMonth == "June" or 
        CurrentMonth == "July" or 
        CurrentMonth == "August"):
    SalesNextMonth = SalesCurrentMonth * 1.20
    return SalesNextMonth
  elif (CurrentMonth == "September" or 
        CurrentMonth == "October" or 
        CurrentMonth == "November"):
    SalesNextMonth = SalesCurrentMonth * 1.25
    return SalesNextMonth
  else:
    print("Invalid Month")

TotalSalesForecast = 0.0
r = input ("Do you want to compute next month's sales forecast? (Y/N)? ")
while r == "Y" or r == "y":
  CurrentMonth = input("Enter the current month: ")
  SalesCurrentMonth = float(input("Enter the total amount of sales for this month: $"))
  SalesNextMonth = ComputeSalesForecast(SalesCurrentMonth, CurrentMonth)
  print("The projected amount of sales for the next month is: $", 
    format(SalesNextMonth, ',.2f'))
  print("")
  r = input ("Do you want to compute another month's sales forecast? (Y/N)? ")

print("Thank you for using the projected sales estimator program!")