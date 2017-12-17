# Uses python3
import random
import sys


def partition2(array, l, r):
    x = array[l]
    m2 = l
    for i in range(l + 1, r + 1):
        if array[i] <= x:
            m2 += 1
            array[i], array[m2] = array[m2], array[i]
    array[l], array[m2] = array[m2], array[l]
    return m2


def randomized_quick_sort_naive(array, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    array[l], array[k] = array[k], array[l]
    # use partition3
    m = partition2(array, l, r)
    randomized_quick_sort(array, l, m - 1)
    randomized_quick_sort(array, m + 1, r)


def partition3(array, l, r):
    x = array[l]
    m1, m2 = l, l
    for i in range(l + 1, r + 1):
        if array[i] == x:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
        if array[i] < x:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
            array[m1], array[m2] = array[m2], array[m1]
            m1 += 1

    return [m1, m2]


def randomized_quick_sort(array, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    array[l], array[k] = array[k], array[l]
    # use partition3
    m1, m2 = partition3(array, l, r)
    randomized_quick_sort(array, l, m1 - 1)
    randomized_quick_sort(array, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    #
    # for j in range(10):
    #     n = random.randint(1, 1e+1)
    #     a = [None] * n
    #     for i in range(n):
    #         a[i] = random.randint(0, 1e+2)

    # a_copy = a.copy()

    # print("n = " + str(n) + "; a = " + str(a))

    # randomized_quick_sort_naive(a, 0, n - 1)
    # randomized_quick_sort(a, 0, n - 1)

    # expected = str(a)
    # actual = str(a)

    # print("Actual: " + str(actual) + "\n")
    # if expected != actual:
    #     pass
