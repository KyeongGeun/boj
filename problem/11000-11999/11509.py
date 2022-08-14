import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

memo = [0 for _ in range(1_000_001)]
cnt = 0
for v in li:
    if memo[v]:
        memo[v] -= 1
        memo[v - 1] += 1
        continue

    memo[v - 1] += 1
    cnt += 1


print(cnt)
