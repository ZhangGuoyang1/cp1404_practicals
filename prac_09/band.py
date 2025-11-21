class Band:
    """Represent a Band that has Musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of band with all musicians."""
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make all musicians in the band play."""
        for musician in self.musicians:
            musician.play()