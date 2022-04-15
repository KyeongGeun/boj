from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

seq = [li[0]]
dp = [1] * n
maxi = 1

for i in range(1, n):
    if seq[-1] < li[i]:
        seq.append(li[i])
        dp[i] = len(seq)
        maxi = len(seq)
    else:
        idx = bisect_left(seq, li[i])
        seq[idx] = li[i]
        dp[i] = idx + 1

print(len(seq))

answer = []
for i in range(n - 1, -1, -1):
    if dp[i] == maxi:
        answer.append(li[i])
        maxi -= 1
print(*answer[::-1])