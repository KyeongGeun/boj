import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n-1, -1, -1):
    if k >= li[i]:
        cnt += k // li[i]
        k %= li[i]
    if k == 0:
        break

print(cnt)