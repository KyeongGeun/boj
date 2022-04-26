import sys
input = sys.stdin.readline


def ccw(A, B, C):
    rt = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    if rt > 0:
        rt = 1
    elif rt < 0:
        rt = -1
    else:
        rt = 0
    return rt


def iscross(l1, l2):
    Ax, Ay, Bx, By = l1
    Cx, Cy, Dx, Dy = l2

    A, B, C, D = (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)

    AB = ccw(A, B, C) * ccw(A, B, D)
    CD = ccw(C, D, A) * ccw(C, D, B)

    if AB > 0 or CD > 0:
        return False
        
    if AB == 0 and CD == 0:
        if A > B:
            A, B = B, A
        if C > D:
            C, D = D, C

        if A <= D and B >= C:
            return True
        else:
            return False

    return True


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

    if x > y:
        x, y = y, x

    parent[x] += parent[y]
    parent[y] = x


n = int(input())

parent = [-1] * n
li = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    li.append((x1, y1, x2, y2))

for i in range(n):
    for j in range(n):
        if i != j and find(i) != find(j) and iscross(li[i], li[j]):
            union(i, j)

group = set()
mmax = 1

for i in range(n):
    p = find(i)
    if -parent[p] > mmax:
        mmax = -parent[p]
    group.add(p)

print(len(group))
print(mmax)
