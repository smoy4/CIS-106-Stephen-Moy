# Stephen Moy
# CIS 106 - W01
# 03/17/2024
# Problem Set 8 - Question 5: Tuition PBV

def ComputeTuition(CreditHours, DistrictCode):
  if DistrictCode == "I":
    Tuition = CreditHours * 250
  elif DistrictCode =="O":
    Tuition = CreditHours * 550
  return Tuition

TotalTuition = 0.0
r = input("Do you want to compute a student's tuition ? (Y/N) ")
while r == "Y" or r == "y":
  StudentLastName = input("Enter the student's last name: ")
  CreditHours = float(input("Enter the number of credit hours: "))
  DistrictCode = input("Enter the student's district code (I or O): ")
  Tuition = ComputeTuition(CreditHours, DistrictCode)
  print("Tuition for Student ", StudentLastName, " is $", Tuition)
  print(" ")
  TotalTuition = TotalTuition + Tuition
  r = input("Do you want to compute another student's tuition ? (Y/N) ")

print("Sum of all Tuitions: $", TotalTuition)
