import sys
input = sys.stdin.readline

def slice(x, y, n, li):
    v = int(li[y][x])+1
    if n == 1:
        cnt[v] += 1
        return

    s = li[y][x]
    flag = False    
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if li[j][i] != s:
                flag = True
            if flag:
                break
        if flag:
            break
    
    if flag:
        for i in range(3):
            for j in range(3):
                slice(x + j*n//3, y + i*n//3, n//3, li)
    else:
        cnt[v] += 1

n = int(input())
li = [input().split() for _ in range(n)]

cnt = [0, 0, 0]
slice(0, 0, n, li)

print(*cnt, sep='\n')