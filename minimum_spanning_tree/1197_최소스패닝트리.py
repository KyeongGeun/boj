import heapq
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

    if x < y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

    return True


v, e = map(int, input().split())

graph = [[] for _ in range(v)]
parent = [-1 for _ in range(v)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a - 1].append((b - 1, w))
    graph[b - 1].append((a - 1, w))

hq = []

a = 0
answer = 0
for _ in range(v - 1):
    for b, w in graph[a]:
        heapq.heappush(hq, (w, b))

    while True:
        w, b = heapq.heappop(hq)
        if union(a, b):
            answer += w
            a = b
            break

print(answer)
