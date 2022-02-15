from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

q = deque()

for _ in range(int(input())):
    s = input().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if q:
            print(q.popleft()+'\n')
        else:
            print('-1'+'\n')
    elif s[0] == 'size':
        print(str(len(q))+'\n')
    elif s[0] == 'empty':
        if q:
            print('0'+'\n')
        else:
            print('1'+'\n')
    elif s[0] == 'front':
        if q:
            print(q[0]+'\n')
        else:
            print(str(-1)+'\n')
    else:
        if q:
            print(q[-1]+'\n')
        else:
            print(str(-1)+'\n')