
print("Danny Thorne")
print("Review")

s = input("Enter a string: ")

# output the characters of the string one by one on separate lines
for c in s:
    print(c)

# output the indices of the characters one by one on separate lines
for i in range(len(s)):
    print(i)

# output the characters and their index side by side for each char
for i in range(len(s)):
    print(s[i],i)

# output True if "a" is in the string
if "a" in s:
    print(True)

# output True if "a" is not in the string
if "a" not in s:
    print(True)

# output the vowels of the string
vowels = "aeiouAEIOU"
for c in s:
    if c in vowels:
        print(c)

# output the third character of the string
print(s[2])

print("--")

# output every third character of the string
# e.g.,
# Enter a string: Hello, World!
# Every third char: l,od
for i in range(len(s)):
    if i%3==2:
        print(s[i])