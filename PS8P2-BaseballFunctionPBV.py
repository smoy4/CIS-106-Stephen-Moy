# Stephen Moy
# CIS 106 - W01
# 03/17/2024

# Problem Set 8 - Problem 2: Baseball Function

def ComputeBattingAverage(PlayerHits, PlayerAtBats):
  PlayerBattingAverage = PlayerHits / PlayerAtBats
  return PlayerBattingAverage
  
NumberPlayers = 0
r = input ("Do you want to compute the player's batting average? (Yes or No)? ")
while r == "Y" or r == "y":
  PlayerLastName = input("Enter the player's last name: ")
  PlayerHits = int(input("Enter the player's number of hits: "))
  PlayerAtBats = int(input("Enter the player's number of times at bat: "))
  print("Player's last name: ", PlayerLastName)
  print("The batting average is: ", format(PlayerBattingAverage, ',.3f'))
  print(" ")
  NumberPlayers = NumberPlayers + 1
  r = input ("Do you want to compute another player's batting average? (Yes or No)? ")

print("The number of players' batting averages processed is: ", NumberPlayers)
