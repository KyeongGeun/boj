import sys
input = sys.stdin.readline

p1x, p1y = map(int, input().split())
p2x, p2y = map(int, input().split())
p3x, p3y = map(int, input().split())

v1 = (p2x - p1x, p2y - p1y)
v2 = (p3x - p1x, p3y - p1y)

m = v1[0] * v2[1] - v1[1] * v2[0]

if m > 0:
    print(1)
elif m < 0:
    print(-1)
else:
    print(0)
