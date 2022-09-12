from collections import deque
import sys
input = sys.stdin.readline


def bfs(temp):
    dq = deque(temp)

    ret = -1
    safe = cnt - len(dq)

    visited = [[False] * n for _ in range(n)]
    for a, b in dq:
        visited[a][b] = True

    while dq:
        ret += 1
        for _ in range(len(dq)):
            x, y = dq.popleft()

            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]

                if a < 0 or a > n - 1:
                    continue
                if b < 0 or b > n - 1:
                    continue
                if li[a][b] == 1:
                    continue
                if visited[a][b]:
                    continue
                visited[a][b] = True

                safe -= 1

                dq.append((a, b))

    if safe > 0:
        return float('inf')
    return ret


def comb(temp, idx):
    if len(temp) == m:
        return bfs(temp)
    if idx > len(virus) - 1:
        return float('inf')

    ret = float('inf')

    temp.append(virus[idx])
    ret = min(ret, comb(temp, idx + 1))
    temp.pop()
    ret = min(ret, comb(temp, idx + 1))
    return ret


n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

cnt = 0

virus = []

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            continue

        cnt += 1
        if li[i][j] == 2:
            virus.append((i, j))

ans = comb([], 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
