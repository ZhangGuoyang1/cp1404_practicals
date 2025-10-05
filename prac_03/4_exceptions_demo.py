"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input data cannot be converted into an integer by int()

2. When will a ZeroDivisionError occur?
When the denominator is 0 and the division is performed

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes. Verify that the denominator is not 0 before performing division.
"""
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Cannot divide by zero")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

print("Finished.")


