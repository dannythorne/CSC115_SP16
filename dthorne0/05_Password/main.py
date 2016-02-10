print("Danny Thorne")
print("Password Example")

correctPassword = "salander"

userPassword = input("Enter a password: ")

if userPassword == correctPassword:
    print("'" + userPassword + "' is the correct password!")

if userPassword != correctPassword:
    print("Sorry, " + userPassword + " is not the correct password.")