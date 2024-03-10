# Stephen Moy
# CIS 106 - W01
# 03/08/2024
# Problem Set 7 - Question 2: Fibonacci Sequence

# This program will print the first 20 numbers of the Fibonacci Sequence.
# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# Fibonacci Sequence ALWAYS starts at 0 and 1.
# However, per Frank Alvino's instructions, the first number is 1 instead of 0.

a = 1 # First number in the sequence (still should be 0).
b = 1
print (a)
print (b)
print (" ")
# start at 1, end at 21, increment of 1 (20 times)
for x in range (1,21,1):
  c = a + b
  print (c)
  a = b 
  b = c
  #prints next 20 numbers after a = 1 and b = 1