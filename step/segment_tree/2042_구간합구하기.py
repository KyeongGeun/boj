import sys
input = sys.stdin.readline


def make(x, i, j):
    if i == j:
        seg[x] = li[i]
        return seg[x]

    mid = (i + j) // 2
    seg[x] = make(x * 2 + 1, i, mid) + make(x * 2 + 2, mid + 1, j)

    return seg[x]


def edit(x, i, j, idx, d):
    if idx < i or j < idx:
        return

    seg[x] += d

    if i == j:
        return

    mid = (i + j) // 2
    edit(x * 2 + 1, i, mid, idx, d)
    edit(x * 2 + 2, mid + 1, j, idx, d)


def ssum(x, i, j, b, c):
    if i > c or j < b:
        return 0
    elif b <= i and j <= c:
        return seg[x]

    mid = (i + j) // 2
    return ssum(x * 2 + 1, i, mid, b, c) + ssum(x * 2 + 2, mid + 1, j, b, c)


n, m, k = map(int, input().split())

li = [int(input()) for _ in range(n)]
seg = [0] * (n * 4)

make(0, 0, n - 1)

ans = []
for _ in range(m + k):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        edit(0, 0, n - 1, b, c - li[b])
        li[b] = c
    elif a == 2:
        c -= 1
        ans.append(ssum(0, 0, n - 1, b, c))

print(*ans, sep='\n')
