def main():
    """this function will print users password into asterisks """
    password = get_password()
    while len(password) >= 0:
        if len(password) > 0:
            hide_password(password)
            break
        password = get_password()


def hide_password(password):
    """this function will convert the letter into asterisks"""
    print('*' * len(password))


def get_password():
    """this function will ask user for their password"""
    password = input("Enter password: ")
    return password


main()