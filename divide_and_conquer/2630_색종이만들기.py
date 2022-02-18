import sys
input = sys.stdin.readline

def quad(x, y, n, li):
    is_only_zero = True
    is_only_one = True

    for i in range(x, x + n):
        for j in range(y, y + n):
            if li[i][j] == '0':
                is_only_one = False
            else:
                is_only_zero = False
    
    if is_only_zero:
        return '0'
    elif is_only_one:
        return '1'
    else:
        return f'({quad(x, y, n//2, li)}{quad(x + n//2, y, n//2, li)}{quad(x, y + n//2, n//2, li)}{quad(x + n//2, y + n//2, n//2, li)})'

n = int(input())
li = [input().split() for _ in range(n)]

q = quad(0, 0, n, li)

print(q.count('0'))
print(q.count('1'))