import numpy as np

print("test")

def normal_integer_random(min_val, max_val, mean, std_dev):
    while True:
        # Generate a normal random value
        normal_val = np.random.normal(mean, std_dev)

        # Round to nearest integer
        int_val = round(normal_val)

        # Check if the value is within the specified range
        if min_val <= int_val <= max_val:
            return int_val


def uniform_integer_random(min_val, max_val):
    # Generate a random integer in the specified range
    return np.random.randint(min_val, max_val)

def exponential_integer_random(min_val, max_val, scale):
    while True:
        # Generate an exponential random value
        value = np.random.exponential(1 / scale)

        # Scale and shift the value to fit within the range
        mapped_value = min_val + int(value) % (max_val - min_val + 1)
        # Check if the value is within the specified range
        if min_val <= mapped_value <= max_val:
            return mapped_value

# Example usage
counter= 0
while (counter <= 5000):
    random_number = uniform_integer_random(1, 100)
    counter = counter + random_number
    print(str(random_number) + ",")

print("****************")

counter= 0
while (counter <= 5000):
    random_number = uniform_integer_random(1, 100)
    counter = counter + random_number
    print(str(random_number) + ",")

