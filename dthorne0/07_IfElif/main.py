print("Danny Thorne")
print("If-Elif-...-Else Example")

temp = input("Enter the temperature in degrees Fahrenheit: ")

temp = int(temp)

if temp>=100:
    print("You might not want to go outside.")
elif temp>=80:
    print("You might want to wear shorts.")
elif temp>=65:
    print("What nice weather. Enjoy!")
elif temp>=35:
    print("You should probably wear a jacket.")
elif temp>=10:
    print("Wear a winter coat and gloves!")
else:
    print("Wow, that's cold. Don't go outside!")

print("Bye, bye!")
