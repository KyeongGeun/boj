import sys
input = sys.stdin.readline


def roll(v):
    if v == 1:
        dice[1], dice[4], dice[6], dice[3] \
            = dice[4], dice[6], dice[3], dice[1]
    elif v == 2:
        dice[1], dice[4], dice[6], dice[3] \
            = dice[3], dice[1], dice[4], dice[6]
    elif v == 3:
        dice[1], dice[2], dice[6], dice[5] \
            = dice[5], dice[1], dice[2], dice[6]
    elif v == 4:
        dice[1], dice[2], dice[6], dice[5] \
            = dice[2], dice[6], dice[5], dice[1]


n, m, x, y, k = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(n)]

li = list(map(int, input().split()))

dice = [0] * 7
ans = []

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for v in li:
    a, b = x + dx[v], y + dy[v]

    if a < 0 or a > n - 1:
        continue
    if b < 0 or b > m - 1:
        continue

    x, y = a, b

    roll(v)

    if table[x][y] == 0:
        table[x][y] = dice[6]
    else:
        dice[6] = table[x][y]
        table[x][y] = 0

    ans.append(dice[1])

print(*ans, sep='\n')
