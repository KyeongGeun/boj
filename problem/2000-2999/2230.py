import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = [int(input()) for _ in range(n)]

li.sort()

l, r = 0, 0

ans = float('inf')
while l <= r < n:
    diff = li[r] - li[l]
    if diff < m:
        r += 1
    elif diff > m:
        ans = min(ans, diff)
        l += 1
    else:
        ans = diff
        break

print(ans)
