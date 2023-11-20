"""CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters something that is not a valid integer when prompted for both the numerator
and denominator.
2. When will a ZeroDivisionError occur? A ZeroDivisionError will occur if the user enters 0 as the denominator because
dividing any number by zero is undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you can add a condition to check whether the denominator is zero before performing the division. If the denominator
is zero, you can handle it gracefully without attempting the division."""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
