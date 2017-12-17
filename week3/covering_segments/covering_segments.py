# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments_):
    points = []
    segments_.sort(key=lambda element: element.end)

    points.append(segments_[0].end)

    for s in segments_:
        if not (s.start <= points[-1] <= s.end):
            points.append(s.end)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # n, *data = map(int, [3, 1, 3, 3, 6, 2, 5])
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # print(segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
