
def banner():
    print("Danny Thorne")
    print("Check for chars in strings...")

def main():
    banner()

    s = "Hello, World!"
    c = "a"

    if c in s:
        print(c+" is in "+s)

    if c not in s:
        print(c+" is not in "+s)

main()