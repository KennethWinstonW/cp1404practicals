"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
Pseudocode 
get sales
while sales >= 0
    calculate bonus
    print bonus
    get sales
"""

BONUS_RATE_LOW = 0.1
BONUS_RATE_HIGH = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * BONUS_RATE_LOW
    else:
        bonus = sales * BONUS_RATE_HIGH
    print(bonus)
    sales = float(input("Enter sales: $"))

