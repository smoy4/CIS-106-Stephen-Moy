# Stephen Moy
# CIS 106 - W01
# 04/11/2024

# Problem Set 11 - Problem 2: Display Last Name Array

def displayarrays(lastname, examscores):
  print("Exam Results for Students (Alphabetical Order): ")
  for i in range (0, 10, 1):
    print("Student ", lastname[i], " has the exam score of ", examscores[i])

lastname = ["Boerner", "Cablarda", "Ciancio", "Cook", "Luba", "Martens", "Melhuse", 
            "Moy", "Qu", "Steeves"]
examscores = [82, 90, 75, 80, 95, 70, 65, 100, 88, 69]

displayarrays(lastname, examscores) 