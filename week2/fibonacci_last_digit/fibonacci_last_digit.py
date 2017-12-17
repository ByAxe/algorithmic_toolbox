# Uses python3


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)

    return current % 10


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    number = int(input())

    # for number in range(1, 327305):
    fast = get_fibonacci_last_digit(number)
    print(fast)
    # slow = get_fibonacci_last_digit_naive(number)
    # if fast != slow:
    #     print("Number " + str(number) + "\tWrong answer: Expected: " + str(slow) + "; Actual: " + str(fast))
    #     break
    # else:
    #     print("Number " + str(number) + "\tOK!\n")
