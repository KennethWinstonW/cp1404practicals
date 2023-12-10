"""
Start: 19:12
End: 19:32
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2023
VINTAGE_YEAR = 50


def main():
    """Tests for Guitar class."""
    gibson_l5_ces = Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40)
    another_guitar = Guitar(name="Another Guitar", year=2013, cost=1000)

    print(f"{gibson_l5_ces.name} get_age() - Expected {95}. Got {gibson_l5_ces.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {5}. Got {another_guitar.get_age()}")
    print()
    print(f"{gibson_l5_ces.name} is_vintage() - Expected {True}. Got {gibson_l5_ces.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


main()
