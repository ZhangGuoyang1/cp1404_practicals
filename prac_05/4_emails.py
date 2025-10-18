def main():
    """Create dictionary of emails-to-names."""
    SPECIAL_CHARACTER = "@"
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        while SPECIAL_CHARACTER not in email:
            print("Error")
            email = input("Email: ")

        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n): ").strip().upper()
        if confirmation != "" and confirmation != "Y":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    print_email(email_to_name)


def print_email(email_to_name):
    """Display names along with their email addresses."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Extract expected name from email address."""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()