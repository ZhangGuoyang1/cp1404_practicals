from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Fancy taxi with higher price and flagfall charge."""

    flagfall = 4.50  # Extra charge for each new fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance.

        fanciness: float that multiplies the price_per_km
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Multiply the base price by fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return string representation with flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the fare including flagfall, rounded to nearest 10c."""
        fare = super().get_fare() + self.flagfall
        return round(fare, 1)