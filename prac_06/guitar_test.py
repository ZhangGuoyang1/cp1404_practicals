from prac_06.guitar import Guitar


def run_test():
    """Test the Guitar class methods with example data."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    # Create two Guitar objects for testing
    guitar_1 = Guitar(name, year, cost)
    guitar_2 = Guitar("Another Guitar", 2012, 1512.9)

    # Test the get_age() method
    print(f"{guitar_1.name} get_age() - Expected {102}. Got {guitar_1.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected {12}. Got {guitar_2.get_age()}")
    print()
    # Test the is_vintage() method
    print(f"{guitar_1.name} is_vintage() - Expected {True}. Got {guitar_1.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected {False}. Got {guitar_2.is_vintage()}")


if __name__ == "__main__":
    run_test()
