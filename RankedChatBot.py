def get_ending(number):
	if number == 1:
		return "st"
	elif number == 2:
		return "nd"
	elif number == 3:
		return "rd"
	else:
		return "th"
i = 0
while i < 5:
	print("iteration: " + str(i + 1) + get_ending(i + 1))
	name = input("Enter your name: ")
	print("Hello, " + name)
	win_ranked = input("How much lp did you gain? ")
	if win_ranked > "0":
		print("lingling40hrs gamer")
	elif win_ranked == "0":
		print("Hurry tf up and climb")
	else:
		print("Hold the L gg=get gud")
	i += 1