# Uses python3
import sys


def get_fibonacci_huge_naive(a, mod):
    if a <= 1:
        return a

    previous = 0
    current = 1

    for _ in range(a - 1):
        previous, current = current, previous + current

    return current % mod


def calc_fib_fast(v):
    if v <= 1:
        return v

    a = [None] * v + [None]

    a[0] = 0
    a[1] = 1

    for i in range(2, v + 1):
        a[i] = a[i - 1] + a[i - 2]

    return a[v]


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


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

    # for _ in range(10000):
    #
    #     n = randint(0, 1e+18)
    #     m = randint(1, 1e+5)
    #
    #     print("FibHuge(n=" + str(n) + ", mod=" + str(m) + ")")
    #
    #     optimal = get_fibonacci_huge(n, m)
    #     print(optimal)
    # naive = get_fibonacci_huge_naive(n, m)
    # if optimal != naive:
    #     print("Wrong answer: Expected: " + str(naive) + "; Actual: " + str(optimal))
    #     break
    # else:
    #     print("OK: Expected: " + str(naive) + "; Actual " + str(optimal) + ";\n")
