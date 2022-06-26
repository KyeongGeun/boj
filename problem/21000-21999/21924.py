import sys
input = sys.stdin.readline


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

    if parent[x] > parent[y]:
        x, y = y, x

    parent[x] += parent[y]
    parent[y] = x

    return True


n, m = map(int, input().split())

parent = [-1] * (n + 1)
graph = []

total = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    total += c
    graph.append((a, b, c))

graph.sort(key=lambda x: x[2])

ans = 0
cnt = 0
for a, b, c in graph:
    if union(a, b):
        ans += c
        cnt += 1

        if cnt == n - 1:
            print(total - ans)
            break
else:
    print(-1)
