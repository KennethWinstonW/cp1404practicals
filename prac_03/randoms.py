import random

print(random.randint(5, 20))  # line 1
# The output will be a random integer between 5 and 20.
# The smallest is 5, and the largest is 20.
print(random.randrange(3, 10, 2))  # line 2
# The output will be a random odd number between 3 and 9.
# The smallest is 3, and the largest is 9.
# No, because the step is 2 (starting from 3), so it would only produce odd numbers.
print(random.uniform(2.5, 5.5))  # line 3
# The output will be a random float between 2.5 and 5.5.
# The smallest is 2.5, and the largest is 5.5.

random_number = random.randint(1, 100)
print(random_number)
