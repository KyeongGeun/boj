from collections import deque
import sys
input = sys.stdin.readline

ans = []

while 1:
    n, *li = list(map(int, input().split()))
    if n == 0:
        break

    dq = deque()
    m = 0

    for i in range(n):
        
        while dq and li[dq[-1]] >= li[i]:
            height = li[dq.pop()]
            if not dq:
                width = i
            else:
                width = i - 1 - dq[-1]
            print(height * width)
            m = max(m, height * width)

        dq.append(i)
    
    i = n
    while dq:
        height = li[dq.pop()]
        if not dq:
            width = i
        else:
            width = i - 1 - dq[-1]
        print(height * width)
        m =  max(m, height * width)

    ans.append(m)

print(*ans, sep='\n')