import random

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0


def main():
    """This function will ask user for their score."""
    score = float(input("Enter score: "))
    determine_grade(score)


def main2():
    """This function will generate a random score between 0 and 100."""
    score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(score)
    determine_grade(score)


def determine_grade(score):
    """This function will help determine the grade based on the score."""
    if score < MINIMUM_SCORE and score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# main()
main2()
