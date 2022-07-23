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


ans = []
for i in range(int(input())):
    ans.append(f"Scenario {i + 1}:")

    n = int(input())

    parent = [-1] * n

    for _ in range(int(input())):
        a, b = map(int, input().split())
        union(a, b)

    for _ in range(int(input())):
        a, b = map(int, input().split())
        if find(a) == find(b):
            ans.append(1)
        else:
            ans.append(0)

    ans.append('')

ans.pop()
print(*ans, sep='\n')
