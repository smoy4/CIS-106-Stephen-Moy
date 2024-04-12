# Stephen Moy
# CIS 106 - W01
# 04/11/2024

# Problem Set 11 - Problem 1: Display Last Name Array

def displayarrays(lastname):
  print("Alphabetical Order:")
  for i in range (0, 10, 1):
    print(lastname[i])

def displayarraysreverse(lastname):
  print("\nReverse Alphabetical Order:")
  for i in range (9, -1, -1):
    print(lastname[i]) 

lastname = ["Boerner", "Cablarda", "Ciancio", "Cook", "Luba", "Martens", "Melhuse", 
            "Moy", "Qu", "Steeves"]

displayarrays(lastname) 
displayarraysreverse(lastname)