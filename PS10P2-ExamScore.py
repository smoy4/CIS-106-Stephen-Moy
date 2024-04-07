# Stephen Moy
# CIS 106 - W01
# 04/04/2024

# Problem Set 10 - Problem 2: Exam Score

def exam_average (exam1,exam2,exam3):
  exampoints = exam1 + exam2 + exam3
  total = 300
  average = format((exampoints / total) * 100, '.2f')
  return exampoints, average
  
lastname = str(input("Enter your last name: "))
exam1 = int(input("Enter your first exam score: "))
exam2 = int(input("Enter your second exam score: "))
exam3 = int(input("Enter your third exam score: "))
exampoints, average = exam_average(exam1,exam2,exam3)
print("Last name: ", lastname)
print("Total Exam points (out of 300): ", exampoints)
print("Youre average exam score is: ", average)