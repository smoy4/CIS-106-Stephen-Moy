# Stephen Moy
# CIS 106 - W01
# 02/09/2024

# Problem Set 3 - Question 1: Total Score of 2 Exams

#Input Phase
Exam1Score = float(input("Enter your Exam 1 score (40% of total score): "))
Exam2Score = float(input("Enter your Exam 2 score (60% of total score): "))

#Process Phase
TotalScore = 0.4 * Exam1Score + 0.6 * Exam2Score

#Output Phase
print("\nYour Total Score: ", TotalScore)