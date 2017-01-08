from y01082f import get_fullname
print("Enter 'a' at any time to quit")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'a':
        break
    last = input("\nPlease geve me a last name: ")
    if last == 'a':
        break
    full_name = get_fullname(first,last)
    print("\tNeatly full_name: " + full_name + ".")
