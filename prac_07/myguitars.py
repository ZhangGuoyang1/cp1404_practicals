from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of programming language details and display"""
    guitars = read_file(FILENAME)
    for guitar in guitars:
        guitars.sort()
        print(guitar)

    name = input("Enter guitar name: ")
    year = input("Enter guitar year: ")
    price = float(input("Enter guitar price: "))
    write_to_file(name, year, price)


def read_file(filename):
    """Get data from external file."""
    guitars = []
    in_file = open(filename, "r")
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


def write_to_file(name, year, price):
    """Add data to external file."""
    with open("guitars.csv", "a") as out_file:
        print(f"{name},{year},{price:,.2f}", file=out_file)


main()