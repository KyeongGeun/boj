from collections import deque
import sys
input = sys.stdin.readline

ans = []

for _ in range(int(input())):
    s = input().rstrip()
    n = int(input())
    dq = deque(input().rstrip()[1:-1].split(','))
    rever = False
    if dq == deque(['']):
        dq.clear()
        
    for v in s:
        if v == 'R':
            rever = not rever
        elif v == 'D':
            if dq:
                if rever:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                ans.append('error')
                break
    else:
        if rever:
            dq.reverse()
            ans.append('['+','.join(dq)+']')
        else:
            ans.append('['+','.join(dq)+']')

print('\n'.join(ans))