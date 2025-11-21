import random
from car import Car


class UnreliableCar(Car):
    """Car that may or may not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance.

        reliability: float between 0 and 100, percentage chance car will drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if random number is less than reliability.

        Returns the distance driven (0 if car doesn't drive).
        """
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0