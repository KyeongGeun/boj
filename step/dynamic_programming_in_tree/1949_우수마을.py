import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

tree = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

visited = [False] * n
visited[0] = True
memo = [[-1, -1] for _ in range(n)]


def dp(x, b):
    if memo[x][b] == -1:
        ssum0 = 0
        ssum1 = 0
        for v in tree[x]:
            if not visited[v]:
                visited[v] = True
                ssum0 += dp(v, 0)
                ssum1 += dp(v, 1)
        memo[x][0] = ssum1
        memo[x][1] = max(ssum0 + li[x], ssum1)

    return memo[x][b]


print(max(dp(0, 0), dp(0, 1)))
