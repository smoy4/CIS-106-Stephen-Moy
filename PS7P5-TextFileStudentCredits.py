# Stephen Moy
# CIS 106 - W01
# 03/08/2024
# Problem Set 7 - Question 5: Read Text File Student Credits

#Input Phase
f = open("dataPS7P5.txt", "r")
c = 0
TotalTuition = 0.0
LastName = str(f.readline().rstrip('\n'))

#Process Phase
while LastName != "": # get first part of the data
  DistrictCode = str(f.readline().rstrip('\n'))
  Credits = float(f.readline())
  if DistrictCode == "I":
    CreditUnitCost = 250.00
  else:
    CreditUnitCost = 500.00
  Tuition = Credits * CreditUnitCost
  c = c + 1
  TotalTuition = TotalTuition + Tuition
  print("Student Last Name: ", LastName)
  print("Credits Taken: ", Credits)
  print("Tuition Owed: $", Tuition)
  print(" ")
  LastName = str(f.readline().rstrip('\n'))

#Output Phase
f.close()
print("Number of Students: ", c)
print("Total Tuition Owed: $", TotalTuition)