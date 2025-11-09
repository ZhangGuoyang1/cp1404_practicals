import datetime

FULL_COMPLETION = 100


class Project:
    def __init__(self, name="", start_date="", priority=int, cost=float, completion=int):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string representation of Project object"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion}%")

    def __repr__(self):
        """Return string representation of Project object"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion}%")

    def is_complete(self):
        """Verify if Project object is complete"""
        return self.completion == FULL_COMPLETION

    def __lt__(self, other):
        """Less than, used for sorting project"""
        return self.priority < other.priority

    def compare_date(self, input_other):
        """Compare the user_input date with project start date."""
        input_date = datetime.datetime.strptime(input_other, "%d/%m/%Y").date()
        return self.start_date >= input_date

    def update_percentage(self, value):
        """Update the project completion percentage."""
        self.completion = value

    def update_priority(self, value):
        """Update the project priority."""
        self.priority = value
