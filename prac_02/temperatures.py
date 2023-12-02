MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """this function will show menu, ask for user choice and convert the value."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            celsius_to_fahrenheit(celsius)
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            fahrenheit = float(input("fahrenheit: "))
            fahrenheit_to_celsius(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    """this function will convert Fahrenheit to Celsius"""
    # Hint: celsius = 5 / 9 * (fahrenheit - 32)
    celsius = 5 / 9 * (fahrenheit - 32)
    # Remove the "pass" statement when you are done. It's a placeholder.
    print(f"Result: {celsius:.2f} F")


def celsius_to_fahrenheit(celsius):
    """this function will convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
