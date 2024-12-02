def integrate_linear_function(m, c, lower_bound, upper_bound):
    """
    Integrates a linear function f(x) = mx + c over a specified range.

    Args:
        m (float): The slope of the linear function.
        c (float): The y-intercept of the linear function.
        lower_bound (float): The lower bound of integration.
        upper_bound (float): The upper bound of integration.

    Returns:
        float: The definite integral of the linear function over the specified range.
    """
    # Antiderivative of mx + c is (m/2)x^2 + cx
    def antiderivative(x):
        return (m / 2) * x**2 + c * x

    # Calculate the definite integral
    return antiderivative(upper_bound) - antiderivative(lower_bound)
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