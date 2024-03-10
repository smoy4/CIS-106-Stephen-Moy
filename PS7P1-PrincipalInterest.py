# Stephen Moy
# CIS 106 - W01
# 03/05/2024

# Problem Set 7 - Question 1: Principal Interest

#Input Phase
p = float(input("Enter the principal amount: $"))
r = float(input("Enter the annual interest rate (in decimal): "))
InterestCumulative = 0

#Process Phase
print(" ")
print("Year    Beginning    Ending")
print("        Balance      Balance")
for count in range(1, 6):
  i = p * r
  eb = p + i
  InterestCumulative = InterestCumulative + i
  #Output Phase
  print(count, "    $", format(p,'.2f'), "    $", format(eb,'.2f'))
  p = eb

print("\nTotal Interest Earned: $", format(InterestCumulative,'.2f'))