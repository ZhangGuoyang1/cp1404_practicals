def get_password(min_length):
    password = input("Enter your password: ")

    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter your password: ")

    return password


def print_asterisks(password):
    print("*" * len(password))


def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)


main()