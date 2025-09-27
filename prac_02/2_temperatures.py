import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

MENU = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"


def main():
    """Main function with menu loop."""
    student_score = -1

    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != 'Q':
        if choice == 'G':
            student_score = get_score()
        elif choice == 'P':
            student_score = validate_score(student_score)
            print(get_grade(student_score))
        elif choice == 'S':
            student_score = validate_score(student_score)
            display_stars(student_score)
        else:
            print("Invalid choice, please try again.")
        print(MENU)
        choice = input("Enter choice:").upper()
    print("Farewell!")


def validate_score(student_score):
    if student_score == -1:
        student_score = get_score()
    return student_score


def display_stars(student_score):
    print(int(student_score) * "*")


def get_valid_score():
    student_score = float(input("Enter score: "))
    while student_score < MINIMUM_SCORE or student_score > MAXIMUM_SCORE:
        print("invalid score")
        student_score = float(input("Enter score: "))
    return student_score


def get_score():
    """Helper to get a score if not set."""
    return get_valid_score()


def get_grade(score):
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Pass"
    else:
        message = "Bad"
    return message


main()
