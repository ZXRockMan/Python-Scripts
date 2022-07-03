import math
wrFile = open("WinsAndLosses.txt", "r")
listofwinsandlosses = wrFile.readlines()
i = 0
max = len(listofwinsandlosses)
wins = 0
loss = 0
while i < max:
	if listofwinsandlosses[i] == "L\n":
		loss += 1
	else:
		wins += 1
	i += 1
print("Number of wins:   " + str(wins))
print("Number of losses: " + str(loss))
winRate = wins / (wins + loss)
winRate = (round(winRate * 1000)/1000)
print("Your winrate is: " + str(winRate * 100) + "%")