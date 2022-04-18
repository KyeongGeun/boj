import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

visited = [False] * n
memo = [[-1, -1] for _ in range(n)]


def dp(x, b):

    if memo[x][b] == -1:
        ssum0 = 0
        ssum1 = 0
        for v in tree[x]:
            if not visited[v]:
                visited[v] = True
                ssum0 += min(dp(v, 0), dp(v, 1))
                ssum1 += dp(v, 1)
        memo[x][0] = ssum1
        memo[x][1] = min(ssum0 + 1, ssum1 + 1)

    return memo[x][b]


visited[0] = True
print(min(dp(0, 1), dp(0, 0)))
