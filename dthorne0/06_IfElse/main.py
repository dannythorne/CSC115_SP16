print("Danny Thorne")
print("If-Else Example")

# Input the user's age and then inform
# them whether or not they are old
# enough to vote. If they are not old
# enough to vote, tell them how many
# years they have left to wait.

usersAge = input("Enter your age: ")

usersAge = int(usersAge)

if usersAge >= 18:
    print("You are old enough to vote!")
else:
    print("You are not yet old enough to vote.")
    print("You have roughly " + str(18-usersAge) + " year(s) left before you can vote.")
