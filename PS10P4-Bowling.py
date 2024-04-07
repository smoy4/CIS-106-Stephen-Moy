# Stephen Moy
# CIS 106 - W01
# 04/04/2024

# Problem Set 10 - Problem 4: Bowling

def computeBowlingAverage(gamescore1, gamescore2, gamescore3, handicap):
  sum = gamescore1 + gamescore2 + gamescore3
  Average = sum / 3
  handicapAverage = (sum + handicap) / 3
  return Average, handicapAverage
  
lastname = str(input("Enter your last name: "))
gamescore1 = float(input("Enter your score for game 1: "))
gamescore2 = float(input("Enter your score for game 2: "))
gamescore3 = float(input("Enter your score for game 3: "))
handicap = float(input("Enter your handicap: "))
Average, handicapAverage = computeBowlingAverage (gamescore1, 
  gamescore2, gamescore3, handicap)

print("\nYour last name: ", lastname)
print("Your average score: ", format(Average, '.2f'))
print("Your handicap average: ", format(handicapAverage, '.2f'))