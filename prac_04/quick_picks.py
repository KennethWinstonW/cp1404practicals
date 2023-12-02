VALUE = 6

import random

amount = int(input("How many quick picks? "))

for i in range(0, amount):
    numbers = []
    for j in range(0, VALUE):
        number = random.randint(1, 45)
        if number in numbers:
            number = random.randint(number+1, 45)
            numbers.append(number)
        else:
            numbers.append(number)
    numbers.sort()
    joined_numbers = (" ".join("{:2d}".format(number) for number in numbers))
    print(f"{joined_numbers}")