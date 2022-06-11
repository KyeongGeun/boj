# 16929
import sys
input = sys.stdin.readline


def dfs(x, y, c):
    cnt[x][y] = c
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        a = x + dx
        b = y + dy

        if a < 0 or a >= n:
            continue
        if b < 0 or b >= m:
            continue
        if li[a][b] != li[x][y]:
            continue

        if cnt[a][b] != -1:
            if cnt[a][b] != cnt[x][y] - 1:
                print('Yes')
                exit(0)
            else:
                continue

        dfs(a, b, c + 1)


n, m = map(int, input().split())

li = [input().rstrip() for _ in range(n)]
cnt = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if cnt[i][j] == - 1:
            dfs(i, j, 0)

print('No')
