import random

print("Danny Thorne")
print("Guess a number -- take 2.")

numToGuess = random.randrange(1,101)
print(numToGuess) # print the guess to facilitate debugging

userGuess = int(input("Guess a number between 1 and 100: ")) # 1. Init LCV

while userGuess!=numToGuess and userGuess>=1 and userGuess<=100: # 2. Condition on LCV
    userGuess = int(input("Guess again: ")) # 3. Update LCV

if userGuess==numToGuess:
    print("Congrats!")
else:
    print("Sorry, that's not a valid guess!")