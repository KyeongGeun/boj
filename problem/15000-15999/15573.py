import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

hq = []
visited = [[False for _ in range(m)] for _ in range(n)]

for j in range(1, m - 1):
    heapq.heappush(hq, (li[0][j], 0, j))
    visited[0][j] = True

for i in range(n):
    for j in (0, m - 1):
        heapq.heappush(hq, (li[i][j], i, j))
        visited[i][j] = True


cnt = 0
d = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while cnt < k:
    c, x, y = heapq.heappop(hq)
    d = max(d, c)

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if a < 0 or a > n - 1:
            continue
        if b < 0 or b > m - 1:
            continue
        if visited[a][b]:
            continue
        visited[a][b] = True

        heapq.heappush(hq, (li[a][b], a, b))

    cnt += 1

print(d)
