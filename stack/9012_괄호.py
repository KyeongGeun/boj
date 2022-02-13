import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    stack = 0
    for v in s:
        if v == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                print('NO')
                break
    else:
        if stack == 0:
            print('YES')
        else:
            print('NO')