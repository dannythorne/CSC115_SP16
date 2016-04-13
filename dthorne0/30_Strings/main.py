
def banner():
    print("Danny Thorne")
    print("Even More with Strings")

def getEvenChars(s):
    print("Inside the function, s = '"+s+"'.")
    s_even = ""
    for i in range(len(s)):
        if i%2==0:
            # append s[i] to s_even in this case
            s_even = s_even + s[i]
            # print(s_even)
    return s_even

def getOddChars(s):
    pass # Exercise

def main():
    banner()
    username = "Danny Thorne"
    print(username)
    print(getEvenChars(username))
    print(getOddChars(username))

main()