# Stephen Moy
# CIS 106 - W01
# 03/21/2024

# Problem Set 9 - Problem 4: Train Fare
def CalculateFare(Miles):
  if Miles >= 30:
    Fare = 12
    return Fare
  elif Miles >= 20:
    Fare = 10
    return Fare
  elif Miles >= 10:
    Fare = 8
    return Fare
  else:
    Fare = 5
    return Fare

SumFares = 0.0
SumPassengers = 0
r = input ("Do you want to compute the train fare? (Y/N)? ")
while r == "Y" or r == "y":
  LastName = input ("Enter your passenger last name: ")
  Miles = int(input("Enter the number of miles from Chicago: "))
  Fare = CalculateFare (Miles)
  print("The fare for", LastName, "is $", Fare)
  print(" ")
  SumFares = SumFares + Fare
  SumPassengers = SumPassengers + 1
  r = input ("Do you want to compute the train fare of another passenger? (Y/N)? ")

print("The sum of all fares is $", format(SumFares, '.2f'))
print("The total number of passengers is", SumPassengers)
print("The average fare is $", format(SumFares/SumPassengers, '.2f'))