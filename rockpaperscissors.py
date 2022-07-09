import random

playerscore = 0
computerscore = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type in Rock/Paper/Scissors or Quit to end: ").lower()
    if user_input == "quit":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
        # rock: 0, paper: 1, scissors: 2
        
    computer_guess = options[random_number]
    print("Computer's chose", computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("You clapped the computer!")
        playerscore += 1
    
    elif user_input == "paper" and computer_guess == "rock":
        print("You clapped the computer!")
        playerscore += 1
    
    elif user_input == "scissors" and computer_guess == "paper":
        print("You clapped the computer!")
        playerscore += 1
              
    else:
        print("You got clapped by the AI!!!")
        computerscore += 1
    print("You won", playerscore, "times.")
    print("The AI won", computerscore, "times.")

              
