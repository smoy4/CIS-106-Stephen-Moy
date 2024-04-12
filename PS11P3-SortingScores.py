# Stephen Moy
# CIS 106 - W01
# 04/11/2024

# Problem Set 11 - Problem 3: Sorting Scores

def loadarrays(lastname,examscore):
  f = open("dataPS11P3.txt", "r")
  for i in range (0,10,1):
    ln = f.readline()
    ln = ln.rstrip("\n")
    lastname.append(ln)
    s = f.readline()
    s.rstrip("\n")
    examscore.append(s)
  f.close()

def highlow(lastname,examscore):
  highscore = 0
  highsubscript = 0
  lowscore = 99999
  lowsubscript = 0
  for i in range (0, 10, 1):
    if float(examscore[i]) > float(highscore):
      highscore = examscore[i]
      highsubscript = i
    elif float(examscore[i]) < float(lowscore):
      lowscore = examscore[i]
      lowsubscript = i
  print("\n")
  print("Section 2 - Highest and Lowest Score Report: ")
  print("Student ",lastname[highsubscript], " has the highest score of ", 
        examscore[highsubscript])
  print("Student ",lastname[lowsubscript], " has the lowest score of ", 
        examscore[lowsubscript])

def displayarrays(lastname, examscore):
  for i in range (0, 10, 1):
    print("Student ", lastname[i], " has the exam score of ", examscore[i])

lastname = []
examscore = []

loadarrays(lastname, examscore)
print("Section 1 - Overall Score Report: ")
displayarrays(lastname,examscore)
highlow(lastname, examscore)