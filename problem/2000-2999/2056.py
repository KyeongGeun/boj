import sys
input = sys.stdin.readline


def dp(i):
    if memo[i] == -1:
        memo[i] = 0
        for v in parent[i]:
            memo[i] = max(memo[i], dp(v))
        memo[i] += time[i]

    return memo[i]


n = int(input())

time = [0] * (n + 1)
parent = [[] for _ in range(n + 1)]
for i in range(n):
    li = list(map(int, input().split()))
    time[i + 1] = li[0]

    for j in range(2, len(li)):
        parent[i + 1].append(li[j])

memo = [-1] * (n + 1)

ans = 0

for i in range(1, n + 1):
    ans = max(ans, dp(i))

print(ans)
