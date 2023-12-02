"""
Pseudocode
make menu
get name
display menu
while choice != Q:
    if choice == H:
        display hello user
    else if choice == G:
        display goodbye user
    else:
        display invalid message
    display menu
    get choice
display finished
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input(">>> ")
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid message")
    print(MENU)
    choice = input(">>> ")
print("Finished.")
