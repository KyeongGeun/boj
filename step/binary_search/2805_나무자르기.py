import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

left, right = 0, max(li)
ans = 0

while left<=right:
    mid = (left + right) // 2
    total = 0

    total = sum(v - mid for v in li if v > mid)
    
    if m <= total:
        left = mid + 1
        ans = mid
    else:
        right = mid -1

print(ans)