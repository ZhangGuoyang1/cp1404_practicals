import random


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    print(get_score_result(score))
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score:.2f} -> {get_score_result(random_score)}")


main()