import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

ans = 0
memo = {}
m, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(m)]

def move(x, y):
    if (x, y) in memo.keys():
        return memo[x, y]
    if x == n - 1 and y == m - 1:
        memo[x, y] = 1
        return 1

    cnt = 0

    if x < n - 1 and li[y][x] > li[y][x + 1]:
        cnt += move(x + 1, y)
    if y < m - 1 and li[y][x] > li[y + 1][x]:
        cnt += move(x, y + 1)
    if x > 0 and li[y][x] > li[y][x - 1]:
        cnt += move(x - 1, y)
    if y > 0 and li[y][x] > li[y - 1][x]:
        cnt += move(x, y - 1)

    memo[x, y] = cnt
    
    return cnt

print(move(0, 0))
