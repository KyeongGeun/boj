import sys
input = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


n = int(input())  # n <= 200
m = int(input())  # m <= 1000

parent = [-1 for _ in range(n + 1)]

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(len(li)):
        if li[j] == 1:
            union(i + 1, j + 1)

route = list(map(int, input().split()))

par = find(route[0])
for i in range(1, len(route)):
    if find(route[i]) != par:
        print('NO')
        break
else:
    print('YES')
