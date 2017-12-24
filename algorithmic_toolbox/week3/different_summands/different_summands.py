# Uses python3
import sys


def out_value(k, l):
    if k <= (2 * l):
        return k
    return l


def optimal_summands(n):
    summands = []

    k = n
    v = 1

    out = 0

    while out < k:
        out = out_value(k, v)
        summands.append(out)
        k -= v
        v += 1

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
