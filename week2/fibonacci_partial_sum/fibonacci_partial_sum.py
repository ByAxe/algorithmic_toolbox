# Uses python3
import sys


def calc_fib_fast(n):
    if n <= 1:
        return n

    a = [None] * n + [None]

    a[0] = 0
    a[1] = 1

    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]

    return a[n]


def get_period_length(mod):
    x = [0, 1]

    for k in range(2, mod * 6):
        x.append((x[k - 1] + x[k - 2]) % mod)
        if x[k] == 1 and x[k - 1] == 0:
            break

    return x


def get_fibonacci_huge(a, mod):
    if a <= 1:
        return a

    if mod == 1:
        return 0

    x = get_period_length(mod)
    period = len(x) - 2

    return x[(a % period)]


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum(from_, to):
    first = get_fibonacci_huge(to + 2, 60)
    second = get_fibonacci_huge(from_ + 1, 60)
    return (first - second) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))

    # for _ in range(10000):
    #     n = 10
    #     m = 0
    #
    #     while n > m:
    #         n = randint(0, 1e+4)
    #         m = randint(0, 1e+4)
    #
    #     print("PartialSum(" + str(n) + "," + str(m) + ")")
    #
    #     optimal = fibonacci_partial_sum(n, m)
    #     naive = fibonacci_partial_sum_naive(n, m)
    #
    #     if optimal != naive:
    #         print("Wrong answer: Expected: " + str(naive) + "; Actual: " + str(optimal))
    #         break
    #     else:
    #         print("OK: Expected: " + str(naive) + "; Actual " + str(optimal) + ";\n")
