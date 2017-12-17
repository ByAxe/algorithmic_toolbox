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


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum(n):
    return (get_fibonacci_huge(n + 2, 60) - 1) % 10
    # return (calc_fib_fast(n + 2) - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    number = int(input)
    print(fibonacci_sum(number))

    # for _ in range(10000):
    #
    #     i = randint(0, 1e+14)
    #
    #     print("LastDigitOfSum(" + str(i) + ")")
    #
    #     optimal = fibonacci_sum(i)
    #     print(optimal)
    # naive = fibonacci_sum_naive(i)

    # if optimal != naive:
    #     print("Wrong answer: Expected: " + str(naive) + "; Actual: " + str(optimal))
    #     break
    # else:
    #     print("OK: Expected: " + str(naive) + "; Actual " + str(optimal) + ";\n")
