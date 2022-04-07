import sys
input = sys.stdin.readline
arr = [input().split() for _ in range(9)]
li = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == '0']

def det(x, y, a):
    for j in range(9):
        if str(a) == arr[x][j]:
            return 0
    for i in range(9):
        if str(a) == arr[i][y]:
            return 0
    x = x//3*3
    y = y//3*3
    for i in range(3):
        for j in range(3):
            if str(a) == arr[x+i][y+j]:
                return 0
    return 1

def sudoku(N):
    if N == len(li):
        print('\n'.join(map(' '.join, arr)))
        exit(0)
    for i in range(1, 10):
        x, y = li[N][0], li[N][1]
        if det(x, y, i):
            arr[x][y] = str(i)
            sudoku(N+1)
            arr[x][y] = '0'

sudoku(0)