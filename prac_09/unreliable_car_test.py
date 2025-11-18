from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class."""
    # Test with 30% reliable car
    unreliable_car = UnreliableCar("Old Bomb", 100, 30)

    print(f"Testing {unreliable_car.name} with {unreliable_car.reliability}% reliability")
    print(f"Initial state: {unreliable_car}")

    # Drive many times to test reliability
    number_of_drives = 100
    successful_drives = 0

    for i in range(number_of_drives):
        # Reset fuel for each test
        unreliable_car.fuel = 10
        distance_driven = unreliable_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1

    success_rate = (successful_drives / number_of_drives) * 100
    print(f"\nDrove {number_of_drives} times, successful: {successful_drives}")
    print(f"Success rate: {success_rate:.1f}%")

    # The success rate should be roughly around the reliability (30%)
    # Allow some variance due to randomness
    assert 10 <= success_rate <= 50, f"Success rate {success_rate}% is outside expected range for 30% reliability"
    print("Test passed: Success rate is within expected range for 30% reliability")

    # Test with 90% reliable car
    reliable_car = UnreliableCar("Almost New", 100, 90)
    print(f"\nTesting {reliable_car.name} with {reliable_car.reliability}% reliability")

    successful_drives = 0
    for i in range(number_of_drives):
        reliable_car.fuel = 10
        distance_driven = reliable_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1

    success_rate = (successful_drives / number_of_drives) * 100
    print(f"Drove {number_of_drives} times, successful: {successful_drives}")
    print(f"Success rate: {success_rate:.1f}%")

    assert 70 <= success_rate <= 100, f"Success rate {success_rate}% is outside expected range for 90% reliability"
    print("Test passed: Success rate is within expected range for 90% reliability")


if __name__ == "__main__":
    main()