def main():
    """Generate a dictionary of email_to_name"""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        user_name = get_name(user_email)
        confirmation = input(f"Is your name {user_name}? (Y/n) ")
        if confirmation.upper() != 'Y' and confirmation != "":
            user_name = input("Name: ")
        email_to_name[user_email] = user_name
        user_email = input("Email: ")


def get_name(user_email):
    """function to separate the name from email"""
    prefix = user_email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
