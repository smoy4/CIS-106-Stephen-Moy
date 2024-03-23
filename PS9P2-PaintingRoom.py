# Stephen Moy
# CIS 106 - W01
# 03/21/2024

# Problem Set 9 - Problem 2: Painting Room

def calculate_paint_gallons(length, width, height):
  SurfaceArea = 2 * (length * height + width * height + length * width)
  NumberGallons = SurfaceArea / 50
  return NumberGallons

r = input ("Do you want to run the paint estimation program(Y/N)? ")
while r == "Y" or r == "y":
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    NumberGallons = calculate_paint_gallons(length, width, height)
    print("The number of gallons of paint needed to paint the room is: ", NumberGallons)
    print("")
    r = input ("Do you want to run the paint estimation program (Yes or No)? ")

print("Thank you for using the paint estimation program.")