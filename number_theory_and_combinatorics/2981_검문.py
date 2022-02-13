import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]

d = []

for i in range(1, n):
    d.append(abs(li[i]-li[i-1]))

g = d[0]
for i in range(1, n-1):
    g = gcd(g, d[i])

s = set()
s.add(g)
for i in range(2, int(g**.5)+1):
    if g%i == 0:
        s.add(i)
        s.add(g//i)

print(*sorted(list(s)))