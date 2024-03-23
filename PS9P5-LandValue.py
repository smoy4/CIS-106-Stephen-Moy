# Stephen Moy
# CIS 106 - W01
# 03/21/2024

# Problem Set 9 - Problem 5: Land Value
def CalculatedAssessedValue(County,MarketValue):
  if County == "Cook":
    AssessedValue = MarketValue * 0.90
  elif County == "DuPage":
    AssessedValue = MarketValue * 0.80
  elif County == "McHenry":
    AssessedValue = MarketValue * 0.75
  elif County == "Kane":
    AssessedValue = MarketValue * 0.60
  else:
    AssessedValue = MarketValue * 0.70
  return AssessedValue

SumMarketValues = 0.0
SumAssessedValues = 0.0

r = input ("Do you want to compute the value of a land parcel? (Yes or No)? ")
while r == "Y" or r == "y":
  County = input ("Enter the county: ")
  MarketValue = float (input ("Enter the market value of the parcel: "))
  AssessedValue = CalculatedAssessedValue(County, MarketValue)
  print("The market value of that parcel is $", format(MarketValue,',.2f'))
  print("The assessed value of that parcel is $", format(AssessedValue, ',.2f'))
  print(" ")
  SumMarketValues = SumMarketValues + MarketValue
  SumAssessedValues = SumAssessedValues + AssessedValue
  r = input ("Do you want to compute the value of another land parcel? (Yes or No)? ")

print("The Sum of all the market values is $", format(SumMarketValues, ',.2f'))
print("The Sum of all the assessed values is $", format(SumAssessedValues, ',.2f'))