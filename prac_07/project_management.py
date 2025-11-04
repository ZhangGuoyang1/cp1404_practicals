from prac_07.project import Project


def main():
    MENU = (
        "Menu:\n(L)oad projects \n(S)ave projects \n(D)isplay projects \n(F)ilter projects by date"
        "\n(A)dd new project \n(U)pdate project \n(Q)uit"
    )

    print("Welcome to Pythonic Project Management")
    projects = get_file('projects.txt')
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_data(projects)

        elif choice == "S":
            save_data(projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            projects = filter_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you for using custom-built project management software.")


def display_project(projects):
    """Display each project details according to incomplete and completed projects."""
    complete_project, incomplete_project = check_project(projects)
    print('Incomplete projects:')
    display_project_details(incomplete_project)
    print("")
    print('Completed projects:')
    display_project_details(complete_project)


def display_project_details(projects):
    """display project details according to incomplete and completed projects."""
    for number, project in enumerate(projects):
        print(f"{number + 1}  {project}")


def update_project(projects):
    """Update project completion percentage according to incomplete and completed projects."""
    projects = sort_projects(projects)
    display_project_details(projects)
    projects_number = {}
    for number, project in enumerate(projects):
        projects_number[str(number + 1)] = project
    try:
        choice = input('Project choice: ')
        chosen_project = projects_number[choice]
        print(chosen_project)
        new_percentage = int(input("New percentage: "))
        new_priority = int(input("New priority: "))

        if new_percentage != '':
            chosen_project.update_percentage(int(new_percentage))

        if new_priority != '':
            chosen_project.update_priority(int(new_priority))

    except KeyError:
        print("Invalid choice")
    return projects


def add_project(projects):
    """Add new project details."""
    print('Lets add a new projects:')
    try:
        name = input('name: ')
        start_date = input('start date(dd/mm/yy): ')
        priority = int(input('priority: '))
        cost = input('Cost estimate: ').replace('$', '')
        cost = float(cost)
        cost = int(cost)
        completion = input('percent complete: ')
        project = Project(str(name), str(start_date), str(priority), str(cost), str(completion))
        projects.append(project)
    except ValueError:
        print("Invalid Input")


def filter_project(projects):
    """Display project than start after user input date."""
    is_valid = False
    while not is_valid:
        try:
            date = input('Show projects that start after date (dd/mm/yy): ')
            filtered_projects_date = []
            for project in projects:
                if project.compare_date(date):
                    filtered_projects_date.append(project)
            projects = sort_projects(filtered_projects_date)
            display_project_details(projects)
            is_valid = True
        except ValueError:
            print("Invalid data format, should be dd/mm/yyyy")
            date = input('Show projects that start after date (dd/mm/yy): ')
    return projects


def save_data(projects):
    """Save projects to user input filename."""
    filename = input('Enter filename to be save: ')
    save_file(projects, filename)


def load_data(projects):
    """Load projects from user input filename."""
    filename = input("Enter filename: ")
    if filename == '':
        try:
            projects = get_file(filename)
            print(projects)
        except FileNotFoundError:
            print("Invalid Filename")
    return projects


def sort_projects(projects):
    """Sort projects by priority."""
    date_list = []
    for project in projects:
        if project.start_date not in date_list:
            date_list.append(project.start_date)
    date_list.sort()
    sorted_project = []
    for date in date_list:
        for project in projects:
            if project.start_date == date:
                sorted_project.append(project)
    return sorted_project


def get_file(filename):
    """Load projects from user input filename."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().replace("\t", ",")
        parts = parts.split(",")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects


def save_file(projects, filename):
    """Save projects to user input filename."""
    with open(filename, 'w') as out_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}",
                  file=out_file)


def check_project(projects):
    """Check if user input date and priority are correct."""
    complete_project = []
    incomplete_project = []
    for project in projects:
        if project in projects:
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    return complete_project, incomplete_project


main()












