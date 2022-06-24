import sys
input = sys.stdin.readline


def calcu(rst, s):
    if s == '.':
        return
    elif s == 'R':
        rst[0] += 1
    elif s == 'G':
        rst[1] += 1
    elif s == 'B':
        rst[2] += 1


n, m, t = map(int, input().split())
clip = [list(input().rstrip()) for _ in range(n)]

rst1 = [0, 0, 0]
for i in range(n):
    calcu(rst1, clip[i][0])
for i in range(1, m):
    calcu(rst1, clip[0][i])

num = min(n - 1, m - 1, t - 1)
for _ in range(num):
    for i in range(n - 1):
        for j in range(m - 1):
            if clip[i][j] != '.':
                continue
            clip[i][j] = clip[i + 1][j + 1]
    for i in range(n):
        calcu(rst1, clip[i][0])
    for i in range(1, m):
        calcu(rst1, clip[0][i])

rst1_1 = [0, 0, 0]
for i in range(n):
    calcu(rst1_1, clip[i][0])
for i in range(1, m):
    calcu(rst1_1, clip[0][i])

if num == t - 1:
    for i in range(3):
        rst1[i] -= rst1_1[i]
else:
    for i in range(3):
        rst1[i] += rst1_1[i] * (t - 1 - num - 1)

rst2 = [0, 0, 0]
for i in range(n):
    for j in range(m):
        calcu(rst2, clip[i][j])

rst = [rst1[i] + rst2[i] for i in range(3)]

print(*rst, sep='\n')
