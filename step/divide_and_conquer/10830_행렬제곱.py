import sys
input = sys.stdin.readline

def mat_mul(mat1, mat2, n):
    mat3 = []
    for i in range(n):
        li = []
        for j in range(n):
            ans = 0
            for k in range(n):
                ans += mat1[i][k] * mat2[k][j]
            ans %= 1000
            li.append(ans)
        mat3.append(li)
    return mat3

def mat_pow(mat, n, b):
    if b == 1:
        return mat_mul(mat, [[1 if i == j else 0 for i in range(n)] for j in range(n)], n)
    mat1 = mat_pow(mat, n, b//2)
    mat2 = mat_mul(mat1, mat1, n)
    if b%2:
        mat2 = mat_mul(mat2, mat, n)
    return mat2

n, b = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

mat = mat_pow(mat, n, b)

for v in mat:
    print(*v)