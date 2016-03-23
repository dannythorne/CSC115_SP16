print("Danny Thorne")
print("First While Loops Example")

# for i in range(n):

n = input("How many time to run the while loop: ")
n = int(n)

i = 0 # 1. Initialize a loop control variable (LCV)
while i<n: # 2. Condition on the LCV
    print(i, end=" ") # do stuff
    i = i + 1 # 3. Update the LCV

print("")
print("Done.")

