# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    left_free_space = capacity
    value = 0.
    size = len(weights)
    ratio = [None] * size

    for i in range(size):
        ratio[i] = values[i] / weights[i]

    while left_free_space != 0:
        max_index, max_value_ratio = max(enumerate(ratio), key=lambda p: p[1])
        weight = weights[max_index]

        if weight > left_free_space:
            weight = left_free_space

        value += weight * max_value_ratio
        left_free_space -= weight

        ratio[max_index] = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = [1, 10, 500, 30]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
