# Uses python3
import sys


def gcd_naive(first, second):
    current_gcd = 1
    for d in range(2, min(first, second) + 1):
        if first % d == 0 and second % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


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


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))

    # c = 0
    # while True:
    #     c = c + 1
    #     print(c)
    #
    #     a = randint(0, 10000000)
    #     b = randint(0, 10000000)
    #
    #     print("GCD(" + str(a) + "," + str(b) + ")")
    #
    #     fast = gcd(a, b)
    #     slow = gcd_naive(a, b)
    #     if fast != slow:
    #         print("Wrong answer: Expected: " + str(slow) + "; Actual: " + str(fast))
    #         break
    #     else:
    #         print("OK: Expected: " + str(slow) + "; Actual " + str(fast) + ";\n")
