PASSWORD_LENGTH = 8


def main():
    """get password and print stars"""
    password = validate_password()
    print(len(password) * "*")


def validate_password():
    """Ask for a valid password"""
    password = input("Enter your password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Enter your password: ")
    return password


main()
