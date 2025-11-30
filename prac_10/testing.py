"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format the phrase as a sentence: capitalised and ending with a full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("python is fun")
    'Python is fun.'
    """
    phrase = phrase.strip()
    phrase = phrase[0].upper() + phrase[1:]
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car_default = Car()
    assert car_default.fuel == 0, "Default fuel is not set correctly"

    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Fuel not set correctly when provided"


run_tests()
doctest.testmod()
