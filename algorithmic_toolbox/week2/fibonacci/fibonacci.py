# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    if n <= 1:
        return n

    a = [None] * n + [None]

    a[0] = 0
    a[1] = 1

    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]

    return a[n]


number = int(input())
# for number in range(1, 30):
fast = calc_fib_fast(number)
print(fast)
# slow = calc_fib(number)
# if fast != slow:
#     print("Number " + str(number) + "\tWrong answer: Expected: " + str(slow) + "; Actual: " + str(fast))
#     break
# else:
#     print("Number " + str(number) + "\tOK!\n")
