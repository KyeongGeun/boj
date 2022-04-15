import sys
input = sys.stdin.readline

st1 = input().rstrip()
st2 = input().rstrip()

dp = [[0 for _ in range(len(st2)+1)] for _ in range(len(st1)+1)]

for i in range(1, len(st1)+1):
  for j in range(1, len(st2)+1):
    if st1[i-1] == st2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(st1)][len(st2)])
