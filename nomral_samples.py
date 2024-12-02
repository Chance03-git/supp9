import numpy as np
def generate_normal_samples(mean, std_dev, num_samples):
    """
    Generates a specified number of samples from a normal distribution with
    a given mean and standard deviation.

    Args:
        mean (float): The mean of the normal distribution.
        std_dev (float): The standard deviation of the normal distribution.
        num_samples (int): The number of samples to generate.

    Returns:
        list: A list of samples from the specified normal distribution.
    """
    if num_samples <= 0:
        raise ValueError("Number of samples must be a positive integer.")
    if std_dev < 0:
        raise ValueError("Standard deviation must be non-negative.")
    
    samples = np.random.normal(mean, std_dev, num_samples)
    return samples.tolist()

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