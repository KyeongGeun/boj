import sys
input = sys.stdin.readline

def dfs(i, j):
    
    li[i][j] = 0
    cnt = 1

    if i != 0 and li[i - 1][j] == '1':
        cnt += dfs(i - 1, j)
    if i != n - 1 and li[i + 1][j] == '1':
        cnt += dfs(i + 1, j)
    if j != 0 and li[i][j - 1] == '1':
        cnt += dfs(i, j - 1)
    if j != n - 1 and li[i][j + 1] == '1':
        cnt += dfs(i, j + 1)

    return cnt
    

n = int(input())
li = [list(input().rstrip()) for _ in range(n)]
cnt = 0
ans = []

for i in range(n):
    for j in range(n):
        if li[i][j] == '1':
            cnt += 1
            ans.append(dfs(i, j))

ans.sort()

print(cnt, *ans, sep='\n')