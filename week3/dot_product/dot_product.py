# Uses python3

import sys


def max_dot_product(a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)

    res = 0
    for i in range(len(a_sorted)):
        res += a_sorted[i] * b_sorted[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [3, 1, 3, -5, -2, 4, 1]
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
