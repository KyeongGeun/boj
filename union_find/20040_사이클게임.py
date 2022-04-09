import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find(x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        print(i)
        sys.exit(0)

    if x < y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[y] = x


# 3 ≤ n ≤ 500,000
# 3 ≤ m ≤ 1,000,000
n, m = map(int, input().split())

parent = [-1] * (n)

for i in range(1, m + 1):
    a, b = map(int, input().split())

    union(a, b)

print(0)
