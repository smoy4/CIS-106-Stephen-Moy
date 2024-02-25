# Stephen Moy
# CIS 106 - W01
# 02/24/2024

# Problem Set 5 - Question 4: Concert Tickets

#Input Phase
print("How many concert tickets would you like to purchase?")
print("Enter the quantity in whole integer format: ")
Ticket_QTY = int(input())

#Process Phase
if Ticket_QTY >= 25:
  Ticket_Price = 50
elif Ticket_QTY >= 10:
  Ticket_Price = 60
elif Ticket_QTY >= 5:
  Ticket_Price = 70
else:
  Ticket_Price = 75
Total = Ticket_QTY * Ticket_Price

#Output Phase
print("\nThe number of tickets you purchased is: " + str(Ticket_QTY))
print("The price per ticket is: $" + str(Ticket_Price))
print("The total cost is: $" + str(Total))