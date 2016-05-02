
def banner():
    print("Danny Thorne")
    print("Introduction to lists.")

def main():
    banner()

    # Lists are specified using square brackets.
    mylist = [] # initialize an empty list
                # (analogous to initializing an empty string)

    # Append items to a list with the .append function on lists.
    mylist.append("milk")
    mylist.append("bread")
    # mylist.append(3.14159265) # possible, but maybe not advisable
    mylist.append("bacon")
    mylist.append("candy")
    mylist.append("eggs")
    mylist.append("rice")

    print(mylist)

    # Access individual items by index just like with strings
    print("mylist[0]: " + mylist[0])
    print("mylist[3]: " + mylist[3])

    # Traverse the items of a list just like with strings:
    print("")
    print("Output the list by item.")
    for item in mylist:
        print(item)

    # Can also traverse the items by index (just as with strings!).
    print("")
    print("Output the items by index.")
    for i in range(len(mylist)):
        print(mylist[i])

    # Check to see if 'bread' is in the list.
    if 'bread' in mylist:
        print("Yes, bread is in the list!")

    # Check to see if an item is /not/ in the list.
    if 'peanuts' not in mylist:
        print("Peanuts is not in the list.")

    # Print out all the four letter words in the list.
    print("")
    print("Four letter words in the list: ")
    for item in mylist:
        if len(item)==4:
            print(item)

main()