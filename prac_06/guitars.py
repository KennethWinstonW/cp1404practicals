"""
Start: 18:47
End: 19:08
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Print the guitar details: name, year, and cost."""
        print(f"{self.name} {self.year} : ${self.cost}")

    def get_age(self):
        """Calculate and return the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is vintage based on its age."""
        return self.get_age() >= VINTAGE_AGE

