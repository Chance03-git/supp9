def solve_system_of_equations(a1, b1, c1, a2, b2, c2):
    """
    Solves a system of two linear equations with two unknowns using Cramer's Rule.

    Args:
        a1 (float): Coefficient of x in the first equation.
        b1 (float): Coefficient of y in the first equation.
        c1 (float): Constant term in the first equation.
        a2 (float): Coefficient of x in the second equation.
        b2 (float): Coefficient of y in the second equation.
        c2 (float): Constant term in the second equation.

    Returns:
        dict: A dictionary with keys 'X' and 'Y' representing the solution, or None if no unique solution exists.
    """
    # Calculate determinants
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # No unique solution

    determinant_x = c1 * b2 - c2 * b1
    determinant_y = a1 * c2 - a2 * c1

    # Calculate x and y
    x = determinant_x / determinant
    y = determinant_y / determinant

    return {"X": x, "Y": y}
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