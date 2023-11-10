import numpy as np

# Sample list of vectors (arrays of numbers)
vectors = [
    np.array([1, 5, 10]),
    np.array([4, 12, 18]),
    np.array([19, 23, 23]),
    np.array([34, 40, 55]),
]

# Target vector to search for
target_vector = np.array([10, 2, 4])

min_distance = 100000000
total_dist = 0

for arr in vectors;
    for i in target_vector.size:
        dist = abs(arr[i] - target_vector[i])
        total_dist += dist
    
    if total_dist < min_distance:
        min_distance = total_dist
        