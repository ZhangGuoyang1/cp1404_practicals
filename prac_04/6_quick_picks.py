import random

RANDOM_NUMBERS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

quick_pick_number = int(input("How many quick picks: "))
while quick_pick_number <= 0:
    print("Quick pick number is > 0")
    quick_pick_number = int(input("How many quick picks: "))

for i in range(quick_pick_number):
    numbers = []
    for j in range(RANDOM_NUMBERS):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in numbers:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number:2d}" for number in numbers))
