def main():
    score = get_valid_score()
    print(f"Your initial score: {score:.2f} -> {get_score_result(score)}")
    MENU = "1. (G)et a valid score \n2. (P)rint result \n3. (S)how stars \n4. (Q)uit"
    print(MENU)
    choice = input("Get choice:")
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
            print(f"Your score: {score:.2f} -> {get_score_result(score)}")
        elif choice == 'P':
            print(f"Score result: {get_score_result(score)}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid choice, please try again.")
        print(MENU)
        choice = input("Get choice:")
    print(f"Farewell! Your final score was: {score:.2f}")
    

def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print('*' * int(score))


def main():
    score = get_valid_score()
    print(f"Your initial score: {score:.2f} -> {get_score_result(score)}")
    MENU = "1. (G)et a valid score \n2. (P)rint result \n3. (S)how stars \n4. (Q)uit"
    print(MENU)
    choice = input("Get choice:")
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
            print(f"Your score: {score:.2f} -> {get_score_result(score)}")
        elif choice == 'P':
            print(f"Score result: {get_score_result(score)}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid choice, please try again.")
        print(MENU)
        choice = input("Get choice:")
    print(f"Farewell! Your final score was: {score:.2f}")


main()