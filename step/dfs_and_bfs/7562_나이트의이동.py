from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = int(input())
    x, y = map(int, input().split())
    x2, y2 = map(int, input().split())

    dq = deque([(x, y)])

    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    visited = [[0 for _ in range(l)] for _ in range(l)]

    while dq:
        x, y = dq.popleft()

        if x == x2 and y == y2:
            print(visited[x][y])
            break

        for i in range(8):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < l and 0 <= b < l:
                if not visited[a][b]:
                    dq.append((a, b))
                    visited[a][b] = visited[x][y] + 1