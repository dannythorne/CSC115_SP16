
def banner():
    print("Danny Thorne")
    print("More about strings.")

def main():
    banner()
    s = "Hello, World!"
    print(s)

    # Here is one way to traverse the characters of a string
    # and do something with each character one by one.
    for c in s:
        print(c) # do stuff with the character

    # Here is a way to get the length of the string.
    print(len(s))

    # Here is another way to traverse the string.
    for i in range(len(s)):
        print("The character at index "+str(i)+" is '"+s[i]+"'.")

main()