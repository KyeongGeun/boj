import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
cnt = 1

li.sort(key=lambda x: (x[1], x[0]))

memo = li[0][1]
for i in range(1, n):
    if memo > li[i][0]:
        continue
    memo = li[i][1]
    cnt += 1

print(cnt)