# Test cases
if __name__ == "__main__":
    # Test 1: Integrating f(x) = 2x + 3 from 0 to 2
    result1 = integrate_linear_function(2, 3, 0, 2)
    print(f"Integral of 2x + 3 from 0 to 2: {result1}")  # Expected: 10.0

    # Test 2: Integrating f(x) = -x + 4 from 1 to 3
    result2 = integrate_linear_function(-1, 4, 1, 3)
    print(f"Integral of -x + 4 from 1 to 3: {result2}")  # Expected: 4.0

    # Test 3: Integrating f(x) = 0x + 0 from 0 to 5
    result3 = integrate_linear_function(0, 0, 0, 5)
    print(f"Integral of 0x + 0 from 0 to 5: {result3}")  # Expected: 0.0