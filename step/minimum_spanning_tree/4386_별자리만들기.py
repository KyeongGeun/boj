import heapq
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


n = int(input())

star = []
graph = [[] for _ in range(n)]
parent = [-1 for _ in range(n)]

for i in range(n):
    a, b = map(float, input().split())
    star.append((a, b))

for i in range(n):
    for j in range(i + 1, n):
        w = get_dist(star[i], star[j])
        graph[i].append((j, w))
        graph[j].append((i, w))

for i in range(n):
    graph[i].sort(key=lambda x: x[1])


hq = []

a = 0
answer = 0
for _ in range(n - 1):
    for b, w in graph[a]:
        heapq.heappush(hq, (w, b))

    while True:
        w, b = heapq.heappop(hq)
        if union(a, b):
            answer += w
            a = b
            break

print('{:.2f}'.format(answer))
