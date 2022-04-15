import sys
input = sys.stdin.readline

n = int(input())

li = [int(input()) for _ in range(n)]

dp = [0]*n

if n == 1:
    print(li[0])
    exit()
elif n == 2:
    print(li[0]+li[1])
    exit()

dp[0] = li[0]
dp[1] = li[0] + li[1]
dp[2] = max(dp[1], li[0]+li[2], li[1]+li[2])

for i in range(3, n): 
    dp[i] = max(dp[i-1], dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i])

print(dp[n-1])