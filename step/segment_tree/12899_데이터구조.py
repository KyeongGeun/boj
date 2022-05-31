import sys
input = sys.stdin.readline


def update(x, s, e, idx):
    if s > idx or e < idx:
        return
    if s == e:
        tree[x] += 1
        return

    mid = (s + e) // 2
    update(x * 2 + 1, s, mid, idx)
    update(x * 2 + 2, mid + 1, e, idx)

    tree[x] = tree[x * 2 + 1] + tree[x * 2 + 2]


def query(th):
    x, s, e = 0, 0, 2000000
    while s != e:
        tree[x] -= 1
        mid = (s + e) // 2
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


tree = [0] * (8000000)

ans = []
for _ in range(int(input())):
    t, x = map(int, input().split())

    if t == 1:
        update(0, 0, 2000000, x)
    elif t == 2:
        ans.append(query(x))

print(*ans, sep='\n')
