from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

d = deque()
ans = ''

for _ in range(int(input())):
    s = input().split()
    if s[0] == 'push_front':
        d.appendleft(s[1])
    elif s[0] == 'push_back':
        d.append(s[1])
    elif s[0] == 'pop_front':
        if d:
            ans += d.popleft() + '\n'
        else:
            ans += '-1\n'
    elif s[0] == 'pop_back':
        if d:
            ans += d.pop() + '\n'
        else:
            ans += '-1\n'
    elif s[0] == 'size':
        ans += str(len(d))+'\n'
    elif s[0] == 'empty':
        if d:
            ans += '0\n'
        else:
            ans += '1\n'
    elif s[0] == 'front':
        if d:
            ans += d[0] + '\n'
        else:
            ans += '-1\n'
    elif s[0] == 'back':
        if d:
            ans += d[-1] + '\n'
        else:
            ans += '-1\n'

print(ans)