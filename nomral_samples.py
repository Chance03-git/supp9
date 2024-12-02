import numpy as np
# Test cases
if __name__ == "__main__":
    # Test 1: Generate 5 samples with mean 0 and standard deviation 1
    samples1 = generate_normal_samples(0, 1, 5)
    print(f"Test 1: Samples: {samples1}")

    # Test 2: Generate 10 samples with mean 10 and standard deviation 2
    samples2 = generate_normal_samples(10, 2, 10)
    print(f"Test 2: Samples: {samples2}")

    # Test 3: Handle invalid input (negative std_dev)
    try:
        generate_normal_samples(0, -1, 5)
    except ValueError as e:
        print(f"Test 3: Exception: {e}")

    # Test 4: Handle invalid input (zero samples)
    try:
        generate_normal_samples(0, 1, 0)
    except ValueError as e:
        print(f"Test 4: Exception: {e}")