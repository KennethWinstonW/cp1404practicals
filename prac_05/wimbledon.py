FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Function to retrieve data, process it, and display results."""
    data = retrieve_data(FILE_NAME)
    champion_stats, participating_countries = process_data(data)
    show_results(champion_stats, participating_countries)


def process_data(data):
    """Create a dictionary of champions and set of countries from data (list of lists)."""
    champion_stats = {}
    participating_countries = set()
    for record in data:
        participating_countries.add(record[INDEX_COUNTRY])
        try:
            champion_stats[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_stats[record[INDEX_CHAMPION]] = 1
    return champion_stats, participating_countries


def show_results(champion_stats, participating_countries):
    """ Display the Wimbledon champions and participating countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_stats.items():
        print(name, count)
    print(f"\nThese {len(participating_countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(participating_countries)))


def retrieve_data(file_name):
    """Get data from the file in list of lists form."""
    data = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


main()
