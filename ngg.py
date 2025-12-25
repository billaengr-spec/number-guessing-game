# number guessing the game

import random
serecret_number = random.randint(1,100)

while True:
    guess=int(input("enter your guess number between 1 to 100:"))
    if guess<serecret_number:
        print("too low! try again.")
        
    elif guess>serecret_number:
        print("too high! try again.")
        
    else:
        print("congratulations! you guessed the number.")
        break