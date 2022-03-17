from copy import deepcopy
import sys
input = sys.stdin.readline
print = sys.stdout.write

v = int(input())
e = int(input())

w = [[float('inf') for _ in range(v)] for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    w[a - 1][b - 1] = min(w[a - 1][b - 1], c)

for i in range(v):
    w[i][i] = 0

d = deepcopy(w)
for k in range(v):
    for i in range(v):
        for j in range(v):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            

for i in range(v):
    for j in range(v):
        if d[i][j] == float('inf'):
            print('0 ')
        else:
            print(str(d[i][j]) + ' ')
    print('\n')