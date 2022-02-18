import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
mat2 = [list(map(int, input().split())) for _ in range(m)]

mat3 = []
for i in range(n):
    li = []
    for j in range(k):
        ans = 0
        for x in range(m):
            ans += mat1[i][x]*mat2[x][j]
        li.append(ans)
    mat3.append(li)

for i in range(n):
    print(' '.join(map(str, mat3[i])))