import sys
input = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parent[x] > parent[y]:
        x, y = y, x

    parent[x] += parent[y]
    parent[y] = x


parent = [-1] * (100_0001)

ans = []
for _ in range(int(input())):
    s = input().split()

    if s[0] == 'I':
        union(int(s[1]), int(s[2]))
    else:
        ans.append(-parent[find(int(s[1]))])

print(*ans, sep='\n')
