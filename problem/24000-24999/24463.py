import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if li[a][b] == '@':
            if a == 0 or a == n - 1 or b == 0 or b == m - 1:
                li[a][b] = '.'
                _print()
                exit()

            li[a][b] = '.'
            dfs(a, b)
            li[a][b] = '@'


def _print():
    ans = [''.join(li[i]) for i in range(n)]
    print(*ans, sep='\n')


n, m = map(int, input().split())
li = [['+' for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

se = []
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '.':
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                se.append((i, j))
            li[i][j] = '@'

li[se[0][0]][se[0][1]] = '.'
dfs(se[0][0], se[0][1])
