from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    dq = deque([(i, j, 0)])
    while dq:
        a, b, c = dq.popleft()

        for i in range(9):
            x = a + dx[i]
            y = b + dy[i]

            if x < 0 or x > 7:
                continue
            if y < 0 or y > 7:
                continue

            if x >= c and li[x - c][y] == '#':
                continue

            if x >= c + 1 and li[x - c - 1][y] == '#':
                continue

            if visited[x][y]:
                continue

            if x == 0 and y == 7:
                return 1

            if a != x and b != y:
                visited[x][y] = True
            dq.append((x, y, c + 1))

    return 0


li = [input().rstrip() for _ in range(8)]
dx = [1, 0, -1, 0, 1, 1, -1, -1, 0]
dy = [0, 1, 0, -1, 1, -1, 1, -1, 0]
visited = [[False for _ in range(8)] for _ in range(8)]

print(bfs(7, 0))
