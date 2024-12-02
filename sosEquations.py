# Test cases
if __name__ == "__main__":
    # Test 1: Unique solution
    result1 = solve_system_of_equations(2, 1, 5, 1, -1, 1)
    print("Test 1:", result1)  # Expected: {'X': 2.0, 'Y': 1.0}

    # Test 2: Parallel lines (no solution)
    result2 = solve_system_of_equations(1, -1, 2, 2, -2, 5)
    print("Test 2:", result2)  # Expected: None

    # Test 3: Coincident lines (infinite solutions)
    result3 = solve_system_of_equations(1, -1, 2, 2, -2, 4)
    print("Test 3:", result3)  # Expected: None