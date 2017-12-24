# Uses python3


# def max_element_slow(array, number):
#     result = 0
#     for v in range(0, number):
#         for j in range(v + 1, number):
#             if array[v] * array[j] > result:
#                 result = array[v] * array[j]
#
#     return result


def max_element(array, number):
    maxElement = 0
    mIdx = 0

    approximatelyMaxElement = 0

    if n == 2:
        return array[0] * array[1]
    else:
        for k in range(0, number):
            if array[k] >= maxElement:
                maxElement = array[k]
                mIdx = k

        for b in range(0, number):
            if array[b] >= approximatelyMaxElement and b != mIdx:
                approximatelyMaxElement = array[b]

        return maxElement * approximatelyMaxElement


n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)
print(max_element(a, n))

# c = 0
# while True:
#     c = c + 1
#     print(c)
#     n = randint(0, 1000)
#     print(n)
#
#     a = [None] * n
#     for i in range(0, n):
#         a[i] = randint(0, 100000)
#     print(a)
#
#     fast = max_element(a, n)
#     slow = max_element_slow(a, n)
#     if fast != slow:
#         print("Wrong answer: Expected: " + str(slow) + "; Actual: " + str(fast))
#         break
#     else:
#          print("OK!\n")
