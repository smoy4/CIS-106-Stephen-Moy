# Stephen Moy
# CIS 106 - W01
# 03/17/2024

# Problem Set 8 - Problem 3: Roadtrip Function

def ComputeMPG(Miles, Gallons):
  MPG = Miles / Gallons
  return MPG

TripsNumber = 0
r = input("Do you want to compute the MPG of a trip? (Y/N) ")
while r == "Y" or r == "y":
  DestinationCity = str(input())
  Miles = int(input())
  Gallons = int(input())
  MPG = ComputeMPG(Miles, Gallons)
  print("Destination City: ", DestinationCity)
  print("Miles: ", Miles)
  print("Miles per gallon: ", MPG)
  print(" ")
  TripsNumber = TripsNumber + 1
  r = input("Do you want to compute the MPG of another trip? (Y/N)")

print("Total Number of Trips: ", TripsNumber)
