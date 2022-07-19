import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = []
for _ in range(n):
    a, b = map(int, input().split())

    if a < b:
        continue

    li.append((b, a))

li.sort(reverse=True)

l, r = li[-1][0], li[-1][1]
li.pop()

ans = m
while li:
    x, y = li.pop()

    if x <= r:
        if r < y:
            r = y
    else:
        ans += (r - l) * 2
        l, r = x, y

ans += (r - l) * 2

print(ans)
