import sys
input = sys.stdin.readline

r, c = map(int, input().split())

li = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

visited = [[False for _ in range(c)] for _ in range(r)]


def dfs(x, y):
    visited[x][y] = True

    for i in range(3):
        a = x + dx[i]
        b = y + dy[i]

        if a < 0 or a > r - 1:
            continue
        if b < 0 or b > c - 1:
            continue
        if li[a][b] == 'x':
            continue
        if visited[a][b]:
            continue
        visited[a][b] = True

        if b == c - 1:
            return True

        if dfs(a, b):
            return True

    return False


ans = 0
for i in range(r):
    if dfs(i, 0):
        ans += 1

print(ans)
