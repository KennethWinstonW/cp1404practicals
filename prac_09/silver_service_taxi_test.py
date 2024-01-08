from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to show how to use car class."""
    taxi = SilverServiceTaxi("Prius 1", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()