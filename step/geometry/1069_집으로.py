import sys
input = sys.stdin.readline

x, y, d, t = map(int, input().split())

dist = (x ** 2 + y ** 2) ** .5

if d <= t:
    print(dist)
    exit(0)

if dist % d == 0:
    print(dist // d * t)
    exit(0)

if dist <= d:
    print(min(t * 2, dist, t + (d - dist)))
    exit(0)

jump = dist // d

dist -= jump * d

print(jump * t + min(t, dist))
