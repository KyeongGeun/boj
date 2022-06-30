import sys
input = sys.stdin.readline

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

li.sort()

l, r = li[0][0], li[0][1]
ans = 0
for i in range(1, n):
    if li[i][0] < r:
        l = min(l, li[i][0])
        r = max(r, li[i][1])
    else:
        ans += r - l
        l = li[i][0]
        r = li[i][1]

ans += r - l

print(ans)
