import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    l, r = 0, 0
    for v in s:
        if v == '(':
            l += 1
        else:
            r += 1
        if r > l:
            print('NO')
            break
    else:
        if l == r:
            print('YES')
        else:
            print('NO')

