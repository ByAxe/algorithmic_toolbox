# Uses python3
import sys


def binary_search(a, key):
    low, high = 0, len(a)

    if key > a[-1] or key < a[0]:
        return -1

    if a[0] == key:
        return 0
    if a[-1] == key:
        return high - 1

    while high != low:
        # if high < low:
        #     return low - 1

        mid = (low + high) // 2

        if key == a[mid]:
            return mid
        elif key < a[mid]:
            high = mid
        else:
            low = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # data = [5, 1, 5, 8, 12, 13, 5, 8, 1, 23, 1, 11]
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
        # linear = linear_search(a, x)
        # binary = binary_search(a, x)
        # if linear != binary:
        #     print("Wrong answer for x=" + str(x) + "; expected: " + str(linear) + "; actual:" + str(binary))
