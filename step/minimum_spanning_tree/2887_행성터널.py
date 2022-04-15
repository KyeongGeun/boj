import sys
input = sys.stdin.readline


def get_dist(x, y):
    return min(abs(x[0] - y[0]), abs(x[1] - y[1]), abs(x[2] - y[2]))


def find(x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if x < y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

    return True


n = int(input())

li = []
parent = [-1 for _ in range(n)]
for i in range(n):
    a, b, c = map(int, input().split())
    li.append((a, b, c, i))

li2 = []

for i in range(3):
    li.sort(key=lambda x: x[i])

    for j in range(1, len(li)):
        li2.append((get_dist(li[j - 1], li[j]), li[j - 1][3], li[j][3]))

li2.sort()

ans = 0
for w, a, b in li2:
    if union(a, b):
        ans += w

print(ans)
