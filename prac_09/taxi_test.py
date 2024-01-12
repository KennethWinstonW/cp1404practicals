from prac_09.taxi import Taxi


def main():
    """Demo test code to show how to use car class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"My taxi has fuel: {my_taxi.fuel}")
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    my_taxi.get_fare()
    print(my_taxi)


main()
