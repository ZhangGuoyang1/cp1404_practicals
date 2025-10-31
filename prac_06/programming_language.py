class ProgrammingLanguage:

    def __init__(self, name="", typing="", is_reflection=False, year=0):
        """Initialize the attribute"""
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        """Return True when typing is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing}, Reflection={self.is_reflection}, {self.year}"
