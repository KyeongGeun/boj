import sys
input = sys.stdin.readline


def init(x, i, j):
    if i == j:
        tree[x] = (li[i], li[i])
        return tree[x]

    mid = (i + j) // 2
    left = init(x * 2 + 1, i, mid)
    right = init(x * 2 + 2, mid + 1, j)

    tree[x] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[x]


def calcu(x, i, j, l, r):
    if i > r or j < l:
        return (float('inf'), -float('inf'))
    elif l <= i and j <= r:
        return tree[x]

    mid = (i + j) // 2
    left = calcu(x * 2 + 1, i, mid, l, r)
    right = calcu(x * 2 + 2, mid + 1, j, l, r)

    return (min(left[0], right[0]), max(left[1], right[1]))


n, m = map(int, input().split())

li = [int(input()) for _ in range(n)]
tree = [(float('inf'), -float('inf'))] * (n * 4)

init(0, 0, n - 1)

ans = []
for _ in range(m):
    a, b = map(int, input().split())
    res = calcu(0, 0, n - 1, a - 1, b - 1)
    ans.append(str(res[0]) + ' ' + str(res[1]))

print('\n'.join(ans))
