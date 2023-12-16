"""
Start: 22:09
End: 22:34
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage object with name, typing, reflection, and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language has a dynamic typing system. Returns a boolean."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
