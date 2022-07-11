from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    cnt = 1
    dq = deque([(x, y)])
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if a < 1 or a > n:
                continue
            if b < 1 or b > n:
                continue
            if (a, b) in road[x][y]:
                continue
            if visited[a][b]:
                continue
            visited[a][b] = True

            if cow[a][b]:
                cnt += 1

            dq.append((a, b))

    return cnt


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, k, r = map(int, input().split())
cow = [[False for _ in range(n + 1)] for _ in range(n + 1)]
road = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(r):
    a, b, c, d = map(int, input().split())
    road[a][b].append((c, d))
    road[c][d].append((a, b))

cows = []
for _ in range(k):
    a, b = map(int, input().split())
    cow[a][b] = True
    cows.append((a, b))

ans = 0
for a, b in cows:
    if visited[a][b]:
        continue
    visited[a][b] = True
    num = bfs(a, b)
    ans += num * (k - num)
print(ans // 2)
