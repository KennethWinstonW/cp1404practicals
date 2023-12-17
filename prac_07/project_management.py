import datetime
from project import Project

MENU = "- (L)oad projects\n - (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"


def main():
    """Main function to run the project management software."""
    in_file = open(FILENAME, 'r')
    data = in_file.readlines()[1:]
    projects = input_date(data)

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "L":
            filename = input("Filename: ")
            in_file = open(filename, 'r')
            new_data = in_file.readlines()[1:]
            projects.extend(input_date(new_data))
            print("Load complete")

        elif choice == "S":
            filename = input("Filename: ")
            save_data(filename, projects)
            print("Save complete")

        elif choice == "D":
            projects.sort()
            show_incomplete_projects(projects)
            show_complete_projects(projects)

        elif choice == "F":
            date = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_projects(date, projects)
            sort_filtered_projects(filtered_projects)

            for project in filtered_projects:
                print(project)

        elif choice == "A":
            print("Let's add a new project")
            name = get_valid_input("Name: ").title()
            start_date = get_valid_start_date()
            priority = get_valid_priority()
            cost_estimate = get_valid_estimate()
            completion_percentage = get_valid_percentage()
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)

        elif choice == "U":
            for i in range(len(projects)):
                project = projects[i]
                print(f"{i} {project}")
            project_choice = get_valid_project_choice(projects)
            chosen_project = projects[project_choice]
            print(chosen_project)
            new_percentage = get_valid_new_number("New percentage: ")
            if new_percentage is not None:
                chosen_project.completion_percentage = new_percentage
            new_priority = get_valid_new_number("New priority: ")
            if new_priority is not None:
                chosen_project.priority = new_priority

        print(MENU)
        choice = input(">>> ").upper()

    save_data(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def input_date(project_data):
    """Converts project data from a list of strings to a list of Project objects."""
    projects = []
    for data in project_data:
        data = data.strip().split("\t")
        projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))
    return projects


def save_data(filename, projects):
    """Saves the list of Project objects to a file."""
    out_file = open(filename, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tPercentage Complete", file=out_file)
    for project in projects:
        print(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
            file=out_file)


def show_incomplete_projects(projects):
    """Prints a list of incomplete projects."""
    print("Incomplete projects")
    for project in projects:
        if not project.is_completed():
            print(" ", project)


def show_complete_projects(projects):
    """Prints a list of complete projects."""
    print("Complete projects")
    for project in projects:
        if project.is_completed():
            print(" ", project)


def get_valid_date(prompt):
    """Prompts the user for a valid date in dd/mm/yyyy format."""
    valid = False
    while not valid:
        try:
            date_string = input(prompt)
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            valid = True
            return date
        except ValueError:
            print("Invalid date, it should be a valid date in dd/mm/yyyy format")


def filter_projects(date, projects):
    """Filters projects based on start date, showing those starting on or after the specified date."""
    filtered_projects = []
    for project in projects:
        project_start_date = datetime.datetime.strptime(project.start_date, "%d,%m%Y").date()
        if project_start_date >= date:
            filtered_projects.append(project)
    return filtered_projects


def sort_filtered_projects(filtered_projects):
    """Sorting filtered projects based on the date"""
    for first_pointer in range(len(filtered_projects)):
        for second_pointer in range(len(filtered_projects)):
            comparison_date = datetime.datetime.strptime(filtered_projects[second_pointer].start_date,
                                                         "%d/%m/%y").date()
        base_date = datetime.datetime.strptime(filtered_projects[first_pointer].start_date, "%d/%m/%Y").date()
        if comparison_date > base_date:
            temporary_storage = filtered_projects[second_pointer]
            filtered_projects[second_pointer] = filtered_projects[first_pointer]
            filtered_projects[first_pointer] = temporary_storage


def get_valid_input(prompt):
    """Getting a valid input from user"""
    answer = input(prompt)
    while input == "":
        print("Input can not be blank")
        answer = input(prompt)
    return answer


def get_valid_start_date():
    """Getting a valid start date"""
    date = get_valid_date("Start date (dd/mm/yy): ")
    start_date = f"{date.strftime('%d/%m/%Y')}"
    return start_date


def get_valid_integer(prompt):
    """Getting a valid integer number"""
    valid = False
    while not valid:
        try:
            number = int(input(prompt))
            valid = True
            return number
        except ValueError:
            print("Invalid input, integer only")


def get_valid_priority():
    """Getting a valid priority number"""
    priority = get_valid_integer("Priority: ")
    while priority <= 0:
        print("Invalid input, must be higher than 0")
        priority = get_valid_integer("Priority: ")
    return priority


def get_valid_float():
    """Getting a valid float or decimal number"""
    valid = False
    while not valid:
        try:
            cost = float(input("Cost estimate: $"))
            valid = True
            return cost
        except ValueError:
            print("Invalid input, numbers only")


def get_valid_estimate():
    """Getting a valid cost estimate"""
    cost_estimate = get_valid_float()
    while cost_estimate < 0:
        print("Invalid input, must be more than $50")
        cost_estimate = float(get_valid_integer("Cost estimate: $"))
    return cost_estimate


def get_valid_percentage():
    """Getting a valid percentage"""
    completion_percentage = get_valid_integer("Percent complete: ")
    while completion_percentage or completion_percentage > 100:
        print("Invalid percentage, between 0% and 100%")
        completion_percentage = get_valid_percentage()
    return completion_percentage


def get_valid_project_choice(projects):
    """Getting a valid project choice"""
    project_choice = get_valid_integer("Project choice: ")
    while project_choice < 0 or project_choice > (len(projects) - 1):
        print("Invalid project choice")
        project_choice = get_valid_integer("Project choice: ")
    return project_choice


def get_valid_new_number(prompt):
    """Get valid new completion percentage or priority"""
    valid = False
    while not valid:
        new_number_string = input(prompt)
    if new_number_string != "":
        try:
            new_number = int(new_number_string)
            if new_number < 0 or new_number > 100:
                print("Invalid number")
            else:
                valid = True
                return new_number
        except ValueError:
            print("Invalid value, integer needed")
    else:
        valid = True


main()

