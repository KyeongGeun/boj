import sys
input = sys.stdin.readline


def init(x, i, j):
    if i == j:
        seg[x] = (li[i], i)
        return seg[x]

    mid = (i + j) // 2
    left = init(x * 2 + 1, i, mid)
    right = init(x * 2 + 2, mid + 1, j)

    if left[0] > right[0]:
        seg[x] = right
    else:
        seg[x] = left

    return seg[x]


def update(x, i, j, idx, val):
    if idx < i or idx > j:
        return seg[x]

    if i == j:
        seg[x] = (val, idx)
        return seg[x]

    mid = (i + j) // 2
    left = update(x * 2 + 1, i, mid, idx, val)
    right = update(x * 2 + 2, mid + 1, j, idx, val)

    if left[0] > right[0]:
        seg[x] = right
    else:
        seg[x] = left

    return seg[x]


def query(x, i, j, p, q):
    if q < i or p > j:
        return (float('inf'), 0)
    elif p <= i and j <= q:
        return seg[x]

    mid = (i + j) // 2
    left = query(x * 2 + 1, i, mid, p, q)
    right = query(x * 2 + 2, mid + 1, j, p, q)

    if left[0] > right[0]:
        return right
    else:
        return left


n = int(input())
li = list(map(int, input().split()))
seg = [(0, 0)] * (n * 4)
init(0, 0, n - 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, 0, n - 1, b - 1, c)
    else:
        print(query(0, 0, n - 1, b - 1, c - 1)[1] + 1)
