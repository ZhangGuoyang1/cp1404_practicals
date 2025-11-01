CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:
    """Represents a guitar with a name, manufacture year, and cost."""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} {self.year} : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return the guitar's age based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage (50 years or older)."""
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        return self.year < other.year
