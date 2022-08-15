from collections import deque
import sys
input = sys.stdin.readline


def out(i, j):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return True
    return False


n, m = map(int, input().split())

li = [list(input().rstrip()) for _ in range(n)]
coin = []

for i in range(n):
    for j in range(m):
        if li[i][j] == 'o':
            coin.append(i)
            coin.append(j)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dq = deque()
dq.append((coin[0], coin[1], coin[2], coin[3]))
visited = [[[[False for _ in range(m)] for _ in range(n)]
            for _ in range(m)] for _ in range(n)]

visited[coin[0]][coin[1]][coin[2]][coin[3]] = True

ans = 0
while dq:
    ans += 1
    if ans > 10:
        break
    for _ in range(len(dq)):
        x, y, z, w = dq.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dx[i]
            d = w + dy[i]

            l, r = out(a, b), out(c, d)

            if l and r:
                continue
            if l or r:
                print(ans)
                exit(0)
            if li[a][b] == '#':
                a, b = x, y
            if li[c][d] == '#':
                c, d = z, w
            if a == c and b == d:
                continue
            if visited[a][b][c][d]:
                continue
            visited[a][b][c][d] = True

            dq.append((a, b, c, d))

print(-1)
