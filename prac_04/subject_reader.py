"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def display_subject_details(data):
    """This function will display subject details"""
    for subject_data in data:
        subject_code, lecturer, num_students = subject_data
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data_list.append(parts)
    input_file.close()
    return data_list


main()