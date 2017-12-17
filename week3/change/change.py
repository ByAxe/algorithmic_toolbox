# Uses python3
import sys


def get_change(s):
    v = s

    if s == 0:
        return s

    tens = int(v / 10)
    v -= tens * 10

    fifth = int(v / 5)
    v -= fifth * 5

    ones = v

    return tens + fifth + ones


if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
