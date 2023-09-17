import numpy as np

# Sample list of vectors (arrays of numbers)
vectors = [
    np.array([1, 2, 3]),
    np.array([4, 5, 6]),
    np.array([7, 8, 9]),
    np.array([10, 11, 12]),
]

# Target vector to search for
target_vector = np.array([11, 2, 4])

# Initialize a variable to store the index of the found vector (if any)
found_index = None

# Perform a linear search
for i, vector in enumerate(vectors):
    if np.array_equal(vector, target_vector):
        found_index = i
        break

if found_index is not None:
    print(f"Target vector found at index {found_index}")
else:
    print("Target vector not found in the list of vectors.")
