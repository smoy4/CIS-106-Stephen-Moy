# Stephen Moy
# CIS 106 - W01
# 02/18/2024

# Problem Set 4 - Question 4: Appliance and Warrantee

#Input Phase
print("What is the name of the appliance?")
ApplianceName = input()
print("What is the cost of the appliance (in USD)?")
ApplianceCost = float(input())

#Process Phase
if ApplianceCost == 0:
  print("Invalid Response. The appliance must cost something!")
  WarranteeCost = 0
elif ApplianceCost > 1000:
  print("A Warrantee cost of 10% of the appliance cost will be added to the total.")
  WarranteeCost = round(0.10 * ApplianceCost,2)
else:
  print("A Warrantee cost of 5% of the appliance cost will be added to the total.")
  WarranteeCost = round(0.05 * ApplianceCost,2)
TotalCost = ApplianceCost + WarranteeCost

#Output Phase
print("\nAppliance Name: " + ApplianceName)
print("Appliance Cost: $" + str(ApplianceCost))
print("Warrantee Cost: $" + str(WarranteeCost))
print("Total Cost: $" + str(TotalCost))