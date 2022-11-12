from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])

    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1
    dq = deque([(0, 0)])
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if a < 0 or a > n - 1:
                continue
            if b < 0 or b > m - 1:
                continue
            if maps[a][b] == 0:
                continue
            if visited[a][b] != -1:
                continue
            visited[a][b] = visited[x][y] + 1
            dq.append((a, b))

    return visited[n - 1][m - 1]
