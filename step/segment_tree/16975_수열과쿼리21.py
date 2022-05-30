import sys
input = sys.stdin.readline


def init(x, s, e):
    if s == e:
        tree[x] = li[s]
        return

    mid = (s + e) // 2
    init(x * 2 + 1, s, mid)
    init(x * 2 + 2, mid + 1, e)


def update(x, s, e, l, r, d):
    if s > r or e < l:
        return
    if l <= s and e <= r:
        tree[x] += (e - s + 1) * d
        if s != e:
            lazy[x * 2 + 1] += d
            lazy[x * 2 + 2] += d
        return

    mid = (s + e) // 2
    update(x * 2 + 1, s, mid, l, r, d)
    update(x * 2 + 2, mid + 1, e, l, r, d)


def query(x, s, e, idx):

    propagate(x, s, e)
    if s > idx or e < idx:
        return 0
    if s == e:
        return tree[x]

    mid = (s + e) // 2
    l = query(x * 2 + 1, s, mid, idx)
    r = query(x * 2 + 2, mid + 1, e, idx)

    return l + r


def propagate(x, s, e):
    if lazy[x]:
        tree[x] += (e - s + 1) * lazy[x]
        if s != e:
            lazy[x * 2 + 1] += lazy[x]
            lazy[x * 2 + 2] += lazy[x]

        lazy[x] = 0


n = int(input())

li = list(map(int, input().split()))
tree = [0] * (n * 4)
lazy = [0] * (n * 4)

init(0, 0, n - 1)

ans = []
for _ in range(int(input())):
    s = list(map(int, input().split()))

    if s[0] == 1:
        update(0, 0, n - 1, s[1] - 1, s[2] - 1, s[3])
    else:
        ans.append(query(0, 0, n - 1, s[1] - 1))

print(*ans, sep='\n')
