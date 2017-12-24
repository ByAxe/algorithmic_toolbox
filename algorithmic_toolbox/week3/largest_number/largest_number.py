# Uses python3

import sys


def is_greater_or_equal(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


def largest_number(v):
    answer = ""

    numbers = v

    while len(numbers) != 0:

        max_digit = 0
        idx = [None]

        for i in range(len(numbers)):
            if is_greater_or_equal(numbers[i], max_digit):
                max_digit = numbers[i]
                idx = i

        answer += str(max_digit)
        del numbers[idx]

    return answer


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    #     data = [3, 21, 2]
    a = data[1:]
    print(largest_number(a))
