"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # Create a car with 180 units of fuel
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create another car named 'Aston Martin' with 100 units of fuel
    limo = Car(100, "Aston Martin")
    limo.add_fuel(20)
    # Try to drive more than the available fuel to test drive logic
    limo.drive(115)
    print(limo.fuel)
    print(limo)


if __name__ == "__main__":
    main()
