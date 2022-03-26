import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

dp = [[1, [li[i]]] for i in range(n)]

maxi = [-float('inf'), -1]
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = dp[j][1] + [li[i]]
    if dp[i][0] > maxi[0]:
        maxi[0] = dp[i][0]
        maxi[1] = i


print(dp[maxi[1]][0])
print(*dp[maxi[1]][1])