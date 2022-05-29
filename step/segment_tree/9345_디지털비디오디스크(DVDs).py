import sys
input = sys.stdin.readline


def init(x, i, j):
    if i == j:
        tree[x] = (li[i], li[i])
        return tree[x]

    mid = (i + j) // 2
    l = init(x * 2 + 1, i, mid)
    r = init(x * 2 + 2, mid + 1, j)

    tree[x] = (min(l[0], r[0]), max(l[1], r[1]))
    return tree[x]


def update(x, i, j, idx, value):
    if i > idx or j < idx:
        return
    if i == j:
        tree[x] = (value, value)
        return

    mid = (i + j) // 2
    update(x * 2 + 1, i, mid, idx, value)
    update(x * 2 + 2, mid + 1, j, idx, value)

    l = tree[x * 2 + 1]
    r = tree[x * 2 + 2]
    tree[x] = (min(l[0], r[0]), max(l[1], r[1]))


def calcu(x, i, j, a, b):
    if i > b or j < a:
        return (float('inf'), -float('inf'))
    if a <= i and j <= b:
        return tree[x]

    mid = (i + j) // 2
    l = calcu(x * 2 + 1, i, mid, a, b)
    r = calcu(x * 2 + 2, mid + 1, j, a, b)

    return (min(l[0], r[0]), max(l[1], r[1]))


ans2 = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    tree = [float('inf'), -float('inf')] * (n * 4)
    li = [i for i in range(n)]

    init(0, 0, n - 1)

    ans = []
    for _ in range(k):
        q, a, b = map(int, input().split())
        if q == 0:
            update(0, 0, n - 1, a, li[b])
            update(0, 0, n - 1, b, li[a])
            li[a], li[b] = li[b], li[a]
        elif q == 1:
            if calcu(0, 0, n - 1, a, b) == (a, b):
                ans.append('YES')
            else:
                ans.append('NO')

    ans2.append('\n'.join(ans))

print('\n'.join(ans2))
