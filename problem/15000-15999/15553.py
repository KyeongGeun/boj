import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li = [int(input()) for _ in range(n)]

li2 = []

for i in range(n - 1):
    li2.append(li[i + 1] - li[i] - 1)

li2.sort()

for _ in range(k - 1):
    li2.pop()

print(n + sum(li2))
