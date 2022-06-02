import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y, d):

    cnt = 0
    if not isclean[x][y]:
        isclean[x][y] = True
        cnt += 1

    for _ in range(4):
        d = (d + 1) % 4

        a = x + dx[d]
        b = y + dy[d]

        if a < 0 or a >= n or b < 0 or b >= m:
            continue

        if li[a][b] == '1' or isclean[a][b]:
            continue

        cnt += dfs(a, b, d)
        break

    else:

        b = (d + 2) % 4

        a = x + dx[b]
        b = y + dy[b]

        if a < 0 or a >= n or b < 0 or b >= m:
            return cnt

        if li[a][b] == '1':
            return cnt

        cnt += dfs(a, b, d)

    return cnt


n, m = map(int, input().split())

r, c, d = map(int, input().split())

if d == 1 or d == 3:
    d = (d + 2) % 4

li = [input().split() for _ in range(n)]

isclean = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

print(dfs(r, c, d))
