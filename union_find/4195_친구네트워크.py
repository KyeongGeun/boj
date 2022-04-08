import sys
input = sys.stdin.readline


def find(x):
    if type(parent[x]) is int and parent[x] < 0:
        return x

    y = find(parent[x])
    parent[x] = y
    return y


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x


for _ in range(int(input())):

    parent = {}
    f = int(input())

    for i in range(f):
        s1, s2 = input().split()

        if s1 not in parent.keys():
            parent[s1] = -1

        if s2 not in parent.keys():
            parent[s2] = -1

        union(s1, s2)
        print(-parent[find(s1)])
