from collections import deque
import sys
input = sys.stdin.readline


def recur(idx, cnt):
    if cnt == 3:
        return bfs()
    if idx > len(blank) - 1:
        return -float('inf')

    ret = -float('inf')
    a, b = blank[idx]
    li[a][b] = 1
    ret = max(ret, recur(idx + 1, cnt + 1))
    li[a][b] = 0
    ret = max(ret, recur(idx + 1, cnt))

    return ret


def bfs():
    visited = [[False] * m for _ in range(n)]

    dq = deque(vi)
    ret = len(blank) - 3
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if a < 0 or a > n - 1:
                continue
            if b < 0 or b > m - 1:
                continue
            if li[a][b] != 0:
                continue
            if visited[a][b]:
                continue
            visited[a][b] = True

            ret -= 1
            dq.append((a, b))

    return ret


n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

blank = []
vi = []

for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            blank.append((i, j))
        elif li[i][j] == 2:
            vi.append((i, j))

print(recur(0, 0))
