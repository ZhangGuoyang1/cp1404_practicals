from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    # Create a SilverServiceTaxi with fanciness of 2
    silver_taxi = SilverServiceTaxi("Limo", 100, 2)

    print(f"Initial state: {silver_taxi}")
    print(f"Price per km: ${silver_taxi.price_per_km:.2f}")

    # Drive 18 km
    silver_taxi.drive(18)

    # Calculate expected fare: 18 * 1.23 * 2 + 4.50 = 48.78, rounded to 48.80
    fare = silver_taxi.get_fare()
    print(f"\nAfter driving 18 km:")
    print(f"{silver_taxi}")
    print(f"Fare: ${fare:.2f}")

    # Test that fare is calculated correctly (rounded to nearest 10c)
    expected_fare = 48.80
    assert fare == expected_fare, f"Expected fare ${expected_fare:.2f}, got ${fare:.2f}"
    print(f"Test passed: Fare is correctly calculated as ${expected_fare:.2f}")

    # Test with Hummer (fanciness of 4)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(f"\nHummer: {hummer}")
    print(f"Hummer price per km: ${hummer.price_per_km:.2f}")

    # Drive 10 km
    hummer.drive(10)
    fare = hummer.get_fare()
    # Expected: 10 * 1.23 * 4 + 4.50 = 49.20 + 4.50 = 53.70
    expected_fare = 53.70
    print(f"After driving 10 km, fare: ${fare:.2f}")
    assert fare == expected_fare, f"Expected fare ${expected_fare:.2f}, got ${fare:.2f}"
    print(f"Test passed: Hummer fare is correctly calculated as ${expected_fare:.2f}")

    # Test start_fare
    hummer.start_fare()
    fare = hummer.get_fare()
    # After starting new fare, only flagfall should apply
    expected_fare = 4.50
    assert fare == expected_fare, f"Expected fare ${expected_fare:.2f}, got ${fare:.2f}"
    print(f"\nTest passed: After start_fare, fare is ${expected_fare:.2f} (flagfall only)")


if __name__ == "__main__":
    main()