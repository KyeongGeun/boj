import sys
input = sys.stdin.readline

def floyd():
    for k in range(v):
        for i in range(v):
            for j in range(v):
                w[i][j] = min(w[i][j], w[i][k] + w[k][j])

v, e = map(int, input().split())

w = [[float('inf') for _ in range(v)] for _ in range(v)]
for i in range(v):
    w[i][i] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    w[a - 1][b - 1] = c

floyd()

mini = float('inf')

for i in range(1, v):
    for j in range(i):
        mini = min(mini, w[i][j] + w[j][i])

print(*w, sep='\n')

if mini == float('inf'):
    print(-1)
else:
    print(mini)