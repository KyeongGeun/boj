from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

t = int(input())

n = int(input())
l1 = [0] + list(map(int, input().split()))
m = int(input())
l2 = [0] + list(map(int, input().split()))

for i in range(2, len(l1)):
    l1[i] += l1[i - 1]
for i in range(2, len(l2)):
    l2[i] += l2[i - 1]

li1, li2 = [], []

for i in range(n):
    for j in range(i + 1, n + 1):
        li1.append(l1[j] - l1[i])
for i in range(m):
    for j in range(i + 1, m + 1):
        li2.append(l2[j] - l2[i])

li1.sort()
li2.sort()

ans = 0
if n < m:
    for v in li1:
        ans += bisect_right(li2, t - v) - bisect_left(li2, t - v)
else:
    for v in li2:
        ans += bisect_right(li1, t - v) - bisect_left(li1, t - v)

print(ans)
