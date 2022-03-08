from collections import deque
import sys
input = sys.stdin.readline

def bfs():

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]

            if 0 <= a < n and 0 <= b < m and 0 <= c < h:
                if li[c][a][b] == 0 or li[c][a][b] > li[z][x][y] + 1:
                    li[c][a][b] = li[z][x][y] + 1
                    q.append((a, b, c))


m, n, h = map(int, input().split()) # 2 <= m, n <= 1000

li = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if li[i][j][k] == 1:
                q.append((j, k, i))

bfs()

maxi = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            maxi = max(maxi, li[i][j][k])
            if li[i][j][k] == 0:
                print(-1)
                sys.exit(0)

print(maxi - 1)