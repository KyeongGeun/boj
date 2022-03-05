import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i, j):

    li[i][j] = 0

    if i != 0 and li[i - 1][j] == 1:
        dfs(i - 1,j)
    if i != n - 1 and li[i + 1][j] == 1:
        dfs(i + 1, j)
    if j != 0 and li[i][j - 1] == 1:
        dfs(i, j - 1)
    if j != m - 1 and li[i][j + 1] == 1:
        dfs(i, j + 1)

ans = []

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    li = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        li[b][a] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                dfs(i, j)
                cnt += 1

    ans.append(cnt)

print(*ans, sep='\n')