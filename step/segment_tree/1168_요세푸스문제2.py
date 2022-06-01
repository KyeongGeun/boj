import sys
input = sys.stdin.readline


def init(x, s, e):
    if s == e:
        tree[x] = 1
        return

    mid = (s + e) // 2
    init(x * 2 + 1, s, mid)
    init(x * 2 + 2, mid + 1, e)

    tree[x] = tree[x * 2 + 1] + tree[x * 2 + 2]


def query(th):
    x, s, e = 0, 0, n - 1

    while s != e:
        mid = (s + e) // 2
        tree[x] -= 1
        if tree[x * 2 + 1] >= th:
            x = x * 2 + 1
            e = mid
        else:
            th -= tree[x * 2 + 1]
            x = x * 2 + 2
            s = mid + 1
    else:
        tree[x] -= 1
        return s


n, k = map(int, input().split())
tree = [0] * (n * 4)

init(0, 0, n - 1)

ans = []
k -= 1
a = k
mod = n
for _ in range(n):
    k %= mod
    idx = query(k + 1)

    ans.append(idx + 1)
    k += a
    mod -= 1

print('<' + ', '.join(map(str, ans)) + '>')
