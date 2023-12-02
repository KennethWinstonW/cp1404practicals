"""
CP1404/CP5632 - Practical
Broken program to determine score status
Pseudocode
get score
if score < 0:
    display invalid score
if else score >= 50 and score <= 90:
    display passable
else:
    display Excellent
"""


# TODO: Fix this!
# score = float(input("Enter score: "))
# if score < 0 and score > 100:
#     print("Invalid score")
# elif score >= 50 and score <= 90:
#     print("Passable")
# else:
#     print("Excellent")

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
if score < 50:
    print("Bad")



