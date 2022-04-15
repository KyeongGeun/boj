import sys
input = sys.stdin.readline

n, c = map(int, input().split())
li = [int(input()) for _ in range(n)]

li.sort()

left, right = 1, li[-1] - li[0]

m = 0

while left <= right:
    mid = (left + right) // 2
    cnt = c - 1

    prev = li[0]
    for i in range(1, n):
        if li[i] - prev >= mid:
            cnt -= 1
            prev = li[i]
            if cnt == 0:
                break

    if cnt == 0:
        left = mid + 1
        m = max(m, mid)
    else:
        right = mid - 1

print(m)