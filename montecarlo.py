import random
from tqdm import tqdm


def simulate_batch_testing(N, p, k):
    total_tests = 0
    for _ in range(N // k):
        batch = [random.random() < p for _ in range(k)]
        if any(batch):
            total_tests += k + 1
        else:
            total_tests += 1
    return total_tests


def find_optimal_k(N, p, k_values, iterations=100):
    optimal_k = k_values[0]
    min_avg_tests = float('inf')

    for k in k_values:
        total_tests_for_k = 0
        for _ in tqdm(range(iterations), desc=f"Simulating for k={k}, p={p}"):
            total_tests_for_k += simulate_batch_testing(N, p, k)
        avg_tests_for_k = total_tests_for_k / iterations
        if avg_tests_for_k < min_avg_tests:
            min_avg_tests = avg_tests_for_k
            optimal_k = k

    return optimal_k, min_avg_tests


# Parameters
N = 10 ** 6  # Total number of samples
p_values = [10 ** -i for i in range(1, 5)]  # Range of p values
k_values = range(1, 101)  # Range of batch sizes to test

# Run simulation for each p and find optimal k
for p in p_values:
    optimal_k, avg_tests = find_optimal_k(N, p, k_values)
    print(f"For p = {p}, optimal batch size k = {optimal_k} with average tests = {avg_tests}")


