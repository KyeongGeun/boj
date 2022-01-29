import sys
input = sys.stdin.readline
arr = []
m, n = map(int, input().split())
def func(a, b):
    cnt1 = 0
    cnt2 = 0
    for i in range(a, a+8):
        for j in range(b, b+8):
            if (i+j)%2 == 0:
                if arr[i][j] == 'B':
                    cnt1 += 1
            else:
                if arr[i][j] == 'W':
                    cnt1 += 1
    for i in range(a, a+8):
        for j in range(b, b+8):
            if (i+j)%2 == 0:
                if arr[i][j] == 'W':
                    cnt2 += 1
            else:
                if arr[i][j] == 'B':
                    cnt2 += 1
    return min(cnt1, cnt2)
arr2 = []
for i in range(m):
    arr.append(input().rstrip())
for i in range(m-7):
    for j in range(n-7):
        arr2.append(func(i, j))
print(min(arr2))