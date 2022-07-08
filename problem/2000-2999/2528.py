import sys
input = sys.stdin.readline


def next(x):
    for i in range(x, n):
        if li[i][2] == 0:
            li[i][0], li[i][1] = li[i][0] + 1, li[i][1] + 1
            if li[i][1] == l:
                li[i][2] = 1
        else:
            li[i][0], li[i][1] = li[i][0] - 1, li[i][1] - 1
            if li[i][0] == 0:
                li[i][2] = 0


n, l = map(int, input().split())

if n == 1:
    print(0)
    exit(0)

li = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    a, b = map(int, input().split())

    if b == 0:
        li[i][0], li[i][1], li[i][2] = 0, a, b
    else:
        li[i][0], li[i][1], li[i][2] = l - a, l, b

i = 0
cnt = 0
while True:
    while li[i][0] <= li[i + 1][1] and li[i][1] >= li[i + 1][0]:
        i += 1
        if i == n - 1:
            print(cnt)
            exit(0)
    next(i)
    cnt += 1
    continue
