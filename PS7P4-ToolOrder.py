# Stephen Moy
# CIS 106 - W01
# 03/08/2024

# Problem Set 7 - Question 4: Tools Order

#Input Phase
f = open("dataPS7P4.txt", "r")
OrdersCount = 0
SumExtendedPrice = 0.0
ToolName = str(f.readline().rstrip('\n'))

#Process Phase
while ToolName != "": # get first part of the data
  ToolQuantity = int(f.readline().rstrip('\n'))
  ToolUnitPrice = float(f.readline().rstrip('\n'))
  ToolExtendedPrice = ToolQuantity * ToolUnitPrice
  OrdersCount = OrdersCount + 1
  SumExtendedPrice = SumExtendedPrice + ToolExtendedPrice
  print("Tool Name: ", ToolName)
  print("Tool Quantity: ", ToolQuantity)
  print("Tool Unit Price: $", format(ToolUnitPrice,'.2f'))
  print("Tool Extended Price: $", format(ToolExtendedPrice,'.2f'))
  print(" ")
  ToolName = str(f.readline().rstrip('\n'))

#Output Phase
f.close()
print("Number of Orders: ", format(OrdersCount,'.2f'))
print("Sum of Extended Prices: $", format(SumExtendedPrice,'.2f'))
print("Average Orders: $", format((SumExtendedPrice / OrdersCount),'.2f'))