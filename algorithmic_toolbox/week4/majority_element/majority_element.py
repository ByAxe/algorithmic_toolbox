# Uses python3
import sys


def get_majority_element_naive(a):
    for i in range(len(a)):
        current_element = a[i]
        count = 0
        for j in range(len(a)):
            if a[j] == current_element:
                count += 1
        if count > n // 2:
            return a[i]
    return -1


def get_majority_element(a, left, right):
    amount = len(a)

    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    dictionary = {}

    for entry in a:
        dictionary[entry] = dictionary.get(entry, 0) + 1

    for k, v in dictionary.items():
        if v > amount // 2:
            return k

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    # for k in range(10000):
    #     print(k)
    #     n = random.randint(1, 1e+5)
    #     a = [None] * n
    #     for i in range(n):
    #         a[i] = random.randint(0, 1e+9)
    #
    #     expected = get_majority_element_naive(a)
    # actual = get_majority_element(a, 0, n)

    # if expected != actual:
    # print("n = " + str(n) + "; a = " + str(a))
    # print("Expected: " + str(expected) + "; Actual: " + str(actual) + "\n")

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
