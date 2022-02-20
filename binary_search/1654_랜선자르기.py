import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]

left, right = 1, max(li)
ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for v in li:
        cnt += v // mid

    if k <= cnt:
        left = mid + 1
        ans = mid
    elif cnt < k:
        right = mid - 1

print(ans)