from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li = [0] * n
cnt = [0] * 21

ans = 0
for i in range(n):
    li[i] = len(input()) - 1
    if i > k:
        cnt[li[i - k - 1]] -= 1

    ans += cnt[li[i]]
    cnt[li[i]] += 1

print(ans)
