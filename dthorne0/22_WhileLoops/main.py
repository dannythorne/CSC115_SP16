import random
print("Danny Thorne")
print("While Loops Example")
print("Guess an integer between 1 and 100 (inclusive).")

numToGuess = random.randrange(1,101)

print("numToGuess = ", numToGuess) # remove this before releasing

guessNotCorrect = True # 1. Initialize LCV

while guessNotCorrect == True: # 2. Condition on the LCV
    userGuess = input("Guess an integer between 1 and 100: ")
    userGuess = int(userGuess)
    if userGuess == numToGuess:
        guessNotCorrect = False # 3. Update LCV
    if userGuess<1:
        guessNotCorrect = False # 3. Update LCV
    if userGuess>100:
        guessNotCorrect = False # 3. Update LCV

if userGuess==numToGuess:
    print("Congratulations! You guess correctly.")
else:
    print("Oops! That's outside the specified range.")