import math
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    li = list(map(int, input().split()))
    dp = [[0 for _ in range(k)] for _ in range(k)]

    for j in range(1, k):
        for i in range(j-1, -1, -1):
            mini = math.inf
            for k in range(j-i):
                mini = min(mini, dp[i][i+k] + dp[i+k+1][j])           
            dp[i][j] = mini + sum(li[i:j+1])
 
    print(dp[0][-1])