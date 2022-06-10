from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    s = deque()
    w = deque()

    for i in range(r):
        for j in range(c):
            if li[i][j] == '*':
                w.append((i, j))
                water[i][j] == True
            elif li[i][j] == 'S':
                s.append((i, j))
                visited[i][j] = True

    cnt = 0
    while s:
        for _ in range(len(w)):
            x, y = w.popleft()
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]

                if a < 0 or a >= r:
                    continue
                if b < 0 or b >= c:
                    continue
                if li[a][b] == 'X':
                    continue
                if li[a][b] == 'D':
                    continue

                if not water[a][b]:
                    water[a][b] = True
                    w.append((a, b))

        cnt += 1
        for _ in range(len(s)):
            x, y = s.popleft()
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]

                if a < 0 or a >= r:
                    continue
                if b < 0 or b >= c:
                    continue
                if li[a][b] == 'X':
                    continue
                if water[a][b]:
                    continue

                if li[a][b] == 'D':
                    return cnt

                if not visited[a][b]:
                    s.append((a, b))
                    visited[a][b] = True

    return 'KAKTUS'


r, c = map(int, input().split())

li = [input().rstrip() for _ in range(r)]
water = [[False for _ in range(c)] for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

print(bfs())
