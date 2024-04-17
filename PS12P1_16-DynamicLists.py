# Stephen Moy
# CIS 106 - W01
# 04/16/2024

# Problem Set 11 - Problems 1 through 16:

def problem1(myList1):
  n = int(input("Enter the Total Number of items for your list: "))
  for n in range(0,n,1):
    s = int(input("Enter an integer: "))
    myList1.append(s)
  return myList1

def displaylist(myList1):
  for item in myList1:
    print(item)

# main
# Problem 1
myList1 = []
myList1 = problem1(myList1)
displaylist(myList1)
print("\nProblem 1: Ask the user for a number n, then ask the user for n numbers.")
print("Store the numbers in a list. Display the list:")
print(myList1)

# Problem 2
myList1.insert(0,99)
print("\nProblem 2: Insert 99 at the beginning of the list:")
print(myList1)

# Problem 3
myList1[0] = 100
print("\nProblem 3: Replace 99 with 100:")
print(myList1)

# Problem 4
myList2 = [500, 600, 700, 800, 900]
myList1.extend(myList2)
print("\nProblem 4: Create second list: [500, 600, 700, 800, 900]")
print(myList1)

# Problem 5
myList1.remove(800)
print("\nProblem 5: Remove 800 from the second list:")
print(myList1)

# Problem 6
myList1.remove(myList1[2])
print("\nProblem 6: Remove the third item in the first list:")
print(myList1)

# Problem 7
myListGrades = ["A", "B", "C", "A", "A", "C"]
print("\nProblem 7: Create a list of grades: A, B, C, A, A, C")
print(myListGrades)

# Problem 8
print("\nProblem 8: Count the number of A grades in the list:")
print("Count of A's: ", myListGrades.count("A"))

# Problem 9
print("\nProblem 9: Display the index of the first B grade:")
print("Index of first B: ", myListGrades.index("B"))

# Problem 10
print("\nProblem 10: Look for a F grade in the list:")
look_for = "F"
if look_for in myListGrades:
  print(str(look_for) + " is at index " + str(myListGrades.index(look_for)))
else:
  print(str(look_for) + " is not in the list.")

# Problem 11
print("\nProblem 11: Clear (but do not delete) the second list:")
del myList2[0:5]
print (myList2)

# Problem 12
print("\nProblem 12: Delete the second list and try to display it.")
del myList2
print("It should give an error message in next line;")
print("REMOVE the # in front of 'print' in the next line of code:")
#print (myList2)

# Problem 13
myListPlayers1 = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print("\nProblem 13: Create and display Players1 list:")
print(myListPlayers1)

# Problem 14
myListPlayers1.sort()
print("\nProblem 14: Sort the Players1 list:")
print(myListPlayers1)

# Problem 15
myListPlayers2 = myListPlayers1.copy()
print("\nProblem 15: Copy the Players1 list to Players2 list:")
print(myListPlayers2)

# Problem 16
myListPlayers2.reverse()
print("\nProblem 16: Reverse the order of the Players2 list:")
print(myListPlayers2)