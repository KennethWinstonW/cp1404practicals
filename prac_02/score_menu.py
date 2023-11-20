MENU = "(G)et\n(P)rint\n(S)how\n(Q)uit"
MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0


def main():
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter score: ", MINIMUM_SCORE, MAXIMUM_SCORE)
            print(f"Your score = {score}")
        elif choice == "P":
            print(f"Your score: {score}")
            result = determine_grade(score)
            print(f"Result: {result}")
        elif choice == "S":
            print(f"You got {score}/{MAXIMUM_SCORE} and here is your star:")
            for i in range(score):
                print("*", end="")
            print()
        else:
            print("Invalid option")
        print()
        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell")


def get_valid_score(prompt, low, high):
    """This function will check if the score that the user gave is valid or not"""
    score = int(input(prompt))
    while score < low or score > high:
        print("invalid score")
        score = int(input(prompt))
    return score


def determine_grade(score):
    """This function will help determine the grade based on the score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
