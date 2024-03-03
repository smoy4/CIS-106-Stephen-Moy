# Stephen Moy
# CIS 106 - W01
# 03/01/2024

# Problem Set 6 - Question 3: Exam Score Average

#Input Phase
print("Do you want to begin this program that calculates exam score averages? (Y/N)")
answer = input()
StudentCount = 0

#Process Phase
while(answer == "Y" or answer == "y" or answer == "Yes" or answer == "YES"):
  print("\nEnter the student's last name:")
  lastName = input()
  print("Please enter the first exam score: ")
  exam1 = int(input())
  print("Please enter the second exam score: ")
  exam2 = int(input())
  examAverage = (exam1 + exam2) / 2
  StudentCount += 1
  print("Student Name: " + lastName)
  print("Exam Average: " + str(examAverage))
  print("Do you want to enter another student's exam scores? (Y/N)")
  answer = input()

#Output Phase
print("\nNumber of students who had their scores averaged: " + str(StudentCount))