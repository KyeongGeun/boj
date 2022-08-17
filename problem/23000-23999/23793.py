import heapq
import sys
input = sys.stdin.readline


def dijk(i, x=0):
    min_d = [float('inf')] * (n + 1)
    min_d[i] = 0

    hq = [(0, i)]
    while hq:
        cur_d, cur_x = heapq.heappop(hq)

        if cur_x == x:
            continue

        if min_d[cur_x] < cur_d:
            continue

        for new_x, d in graph[cur_x]:
            new_d = cur_d + d
            if min_d[new_x] > new_d:
                min_d[new_x] = new_d
                heapq.heappush(hq, (new_d, new_x))

    return min_d


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

x, y, z = map(int, input().split())

min_x = dijk(x, y)
min_y = dijk(y)

ans = [min_x[y] + min_y[z], min_x[z]]
for i in range(2):
    if ans[i] == float('inf'):
        ans[i] = -1

print(*ans)
