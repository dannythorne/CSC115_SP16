print("Danny Thorne")
print("While Loops Example")

s = 0 # variable to accumulate a sum

n = int(input("Enter a number (negative to quit):")) # 1. Init LCV
while n>=0: # 2. Condition on LCV
    print("You entered " + str(n) + ".") # do stuff
    s = s + n # increment the sum s by the amount n
    n = int(input("Enter a number (negative to quit):")) # 3. Update LCV

print("s = " + str(s))
print("Thanks. Bye!")
