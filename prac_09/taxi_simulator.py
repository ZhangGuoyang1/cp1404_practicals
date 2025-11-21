from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")

    choice = ""
    while choice.lower() != "q":
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ")

        if choice.lower() == "q":
            break
        elif choice.lower() == "c":
            current_taxi = choose_taxi(taxis)
        elif choice.lower() == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    # Final summary
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display available taxis and let user choose one."""
    print("Taxis available: ")
    display_taxis(taxis)

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            selected_taxi = taxis[choice]
            selected_taxi.start_fare()  # Start a new fare when choosing taxi
            return selected_taxi
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None


def display_taxis(taxis):
    """Display all taxis with their index numbers."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi):
    """Drive the selected taxi and return the fare."""
    try:
        distance = float(input("Drive how far? "))
        taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0.0


if __name__ == "__main__":
    main()