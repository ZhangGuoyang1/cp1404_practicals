from prac_07.project import Project


def main():
    """Control the main menu for managing projects."""
    MENU = (
        "- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date"
        "\n- (A)dd new project  \n- (U)pdate project\n- (Q)uit"
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
            filter_project(projects)
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
    incomplete_project, complete_project = check_project(projects)
    print('Incomplete projects: ')
    display_project_details(incomplete_project)
    print('Completed projects: ')
    display_project_details(complete_project)


def display_project_details(projects):
    """display project details according to incomplete and completed projects."""
    sorted_projects = sorted(projects)
    for project in sorted_projects:
        print(f"  {project}")


def update_project(projects):
    """Update project completion percentage according to incomplete and completed projects."""
    sorted_projects = sort_projects(projects)
    for number, project in enumerate(sorted_projects):
        print(f"{number} {project}")

    try:
        choice = input('Project choice: ')
        project_index = int(choice)
        chosen_project = sorted_projects[project_index]
        print(chosen_project)

        new_percentage = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_percentage != '':
            chosen_project.update_percentage(int(new_percentage))

        if new_priority != '':
            chosen_project.update_priority(int(new_priority))

    except KeyError:
        print("Invalid choice")
    return projects


def add_project(projects):
    """Add new project details."""
    print("Let's add a new project")
    try:
        name = input('Name: ')
        start_date = input('Start date (dd/mm/yy): ')
        priority = int(input('Priority: '))
        cost = input('Cost estimate: ').replace('$', '')
        cost = float(cost)
        completion = int(input('Percent complete: '))
        project = Project(str(name), str(start_date), priority, cost, completion)
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
            sorted_projects = sort_projects(filtered_projects_date)
            for project in sorted_projects:
                print(project)
            is_valid = True
        except ValueError:
            print("Invalid data format, should be dd/mm/yyyy")


def save_data(projects):
    """Save projects to user input filename."""
    filename = input('Enter filename to be save: ')
    save_file(projects, filename)


def load_data(projects):
    """Load projects from user input filename."""
    filename = input("Enter filename: ")
    if filename != '':
        try:
            projects = get_file(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
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
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}"
                  f"\t{project.completion}", file=out_file)


def check_project(projects):
    """Check if projects are complete or incomplete."""
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












