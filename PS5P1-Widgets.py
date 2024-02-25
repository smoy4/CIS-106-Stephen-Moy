# Stephen Moy
# CIS 106 - W01
# 02/24/2024

# Problem Set 5 - Question 1: Widgets

#Input Phase
print("Enter the number of widgets you want to order: ")
WidgetQTY = int(input())

#Process Phase
if WidgetQTY > 10000: 
  WidgetUnitPrice = 10
elif WidgetQTY >= 5000:
  WidgetUnitPrice = 20
else:
  WidgetUnitPrice = 30
ExtendedPrice = WidgetQTY * WidgetUnitPrice
Tax = round(ExtendedPrice * 0.07,2)
Total = ExtendedPrice + Tax

#Output Phase
print("\nExtended Price: $", ExtendedPrice)
print("Tax: $", Tax)
print("Total: $", Total)