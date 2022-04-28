import sys
input = sys.stdin.readline

bit = 0b0

for _ in range(int(input())):
    s = input().split()
    if s[0] == 'all':
        bit = 1048575
    elif s[0] == 'empty':
        bit = 0
    else:
        n = int(s[1]) - 1
        if s[0] == 'add':
            bit |= 2 ** n
        elif s[0] == 'remove':
            bit &= 1048575 - 2 ** n
        elif s[0] == 'check':
            print(1 if bit & 2 ** n == 2 ** n else 0)
        else:
            bit ^= 2 ** n
