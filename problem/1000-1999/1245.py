import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]
li = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y):
    visited[x][y] = True
    k = li[x][y]

    flag = True
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()

        for i in range(8):
            a = x + dx[i]
            b = y + dy[i]

            if a < 0 or a > n - 1:
                continue
            if b < 0 or b > m - 1:
                continue
            if li[a][b] > k:
                flag = False

            if not visited[a][b] and li[a][b] == k:
                stack.append((a, b))
                visited[a][b] = True

    return flag


ans = 0
for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            continue
        if visited[i][j]:
            continue
        if dfs(i, j):
            ans += 1

print(ans)
