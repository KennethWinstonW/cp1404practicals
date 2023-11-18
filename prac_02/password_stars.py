def main():
    password = get_password()
    while len(password) >= 0:
        if len(password) > 0:
            hide_password(password)
            break
        password = get_password()


def hide_password(password):
    print('*' * len(password))


def get_password():
    password = input("Enter password: ")
    return password


main()