import sys
input = sys.stdin.readline


def get_dist(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** .5


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


n, m = map(int, input().split())

v = []
for _ in range(n):
    a, b = map(int, input().split())
    v.append((a, b))

parent = [-1 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

graph = []

for i in range(n):
    for j in range(i + 1, n):
        graph.append((i, j, get_dist(v[i], v[j])))

graph.sort(key=lambda x: x[2])

answer = 0
for a, b, w in graph:
    if union(a, b):
        answer += w
        m += 1
        if m == n - 1:
            break

print('{:.2f}'.format(answer))
