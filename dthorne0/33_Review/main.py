import string

def banner():
    print("Danny Thorne")
    print("Review")

# Write a function named removePunctuation that has a string
# parameter s and returns a string consisting of the characters
# of s with punctuation removed.
def removePunctuation(s):
    snew = ""
    print("Removing punctuation from "+s+"!")
    print("Punctuation: " + string.punctuation)
    for c in s:
        if c not in string.punctuation:
            snew = snew + c
    return snew

# Write a function named maskCase that takes a string parameter
# and returns a string (optional: with punctuation and white space removed
# and) with a capital "X" in place of capital letters and a hyphen
# "-" in place of lower case letters.
# e.g.,
# Enter a string: Hello, World!
# Masked string : X----, X----!
def maskCase(s):
    snew = ""
    for c in s:
        if c in string.ascii_lowercase:
            snew = snew + "-"
        elif c in string.ascii_uppercase:
            snew = snew + "X"
        else:
            snew = snew + c
    return snew

def main():
    banner()

    sansPunct = removePunctuation("Hello, World!")
    print("Sans punctuation: " + sansPunct)
    sansPunct = removePunctuation("Red, Green, and Blue!")
    print("Sans punctuation: " + sansPunct)

    print(maskCase("Hello, World!"))

main()