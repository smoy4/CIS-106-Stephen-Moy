# Stephen Moy
# CIS 106 - W01
# 04/11/2024

# Problem Set 11 - Problem 4: Searching Batting Averages

def loadarrays(lastname,battingaverage):
  f = open("dataPS11P4.txt", "r")
  for i in range (0,10,1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    lastname.append(ln)
    s = f.readline()
    s.rstrip("\n")
    battingaverage.append(s)
  f.close()

def displayarrays(lastname, battingaverage):
  for i in range (0, 10, 1):
    print("Player ", lastname[i], " has the batting average of ", battingaverage[i])

def searchname(lastname,battingaverage,searchlastname):
  foundsubscript = -1 
  for i in range(0,10,1):
    if lastname[i] == searchlastname:
      foundsubscript = i
  if foundsubscript == -1:
    print("") # Included as filler for IF statement
      # For Problem 4, no message prints if the name is not found.
  else:
    print("Player ",lastname[foundsubscript], " has a score of ", 
          battingaverage[foundsubscript])

lastname = []
battingaverage = []
loadarrays(lastname, battingaverage)
print("2024 Chicago White Sox Batting Averages")
print("\nSection 1 - Overall Batting Averages Report: ")
displayarrays(lastname, battingaverage)

print("\nSection 2 - Search Batting Average Function: ")
response = input ("Do you want to search for a last name? (Y or N) ")
while response == "Y" or response == "y":
  searchlastname = input("Enter the last name you want to search for: ")
  searchname(lastname, battingaverage, searchlastname)
  response = input("Do you want to search for a last name? (Y or N)")

print("Thank you for using search exam score program! Goodbye!")