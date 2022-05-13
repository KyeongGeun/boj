import sys
input = sys.stdin.readline

m = int(input())

f = [[-1 for _ in range(m + 1)] for _ in range(18)]
f[0] = [0] + list(map(int, input().split()))

for i in range(1, 18):
    for j in range(1, m + 1):
        f[i][j] = f[i - 1][f[i - 1][j]]

q = int(input())

for _ in range(q):
    n, x = map(int, input().split())

    z = 17

    while z >= 0:
        if n >= 2 ** z:
            x = f[z][x]
            n -= 2 ** z
        else:
            z -= 1

    print(x)
