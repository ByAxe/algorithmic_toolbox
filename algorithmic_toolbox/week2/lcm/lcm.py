# Uses python3
import sys
from fractions import Fraction


def gcd(first, second):
    a = first
    b = second

    if a == 0 or b == 0:
        return 1

    if a == b:
        return a

    a_ = a % b

    if a % b == 0:
        return b

    while a % b != 0:
        a_ = a % b
        a = b
        b = a_

    return a_


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm(a, b):
    return Fraction((a * b), gcd(a, b))


if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

    # c = 0
    # for _ in range(10000):
    #     c = c + 1
    #     print(c)
    #
    #     maximal = 2 * 1e+3
    #
    #     a = randint(1, maximal)
    #     b = randint(1, maximal)
    #
    #     print("LCM(" + str(a) + "," + str(b) + ")")
    #
    #     fast = lcm(a, b)
    #     slow = lcm_naive(a, b)
    #     if fast != slow:
    #         print("Wrong answer: Expected: " + str(slow) + "; Actual: " + str(fast))
    #         break
    #     else:
    #         print("OK: Expected: " + str(slow) + "; Actual " + str(fast) + ";\n")
