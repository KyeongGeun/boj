from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    memo = [-1] * 10000
    a, b = map(int, input().split())
    dq = deque([(a, '')])

    cnt = 0
    while dq:
        num, s = dq.popleft()

        dslr = []
        dslr.append((((num * 2) % 10000), s + 'D'))
        dslr.append((((num - 1) % 10000), s + 'S'))
        dslr.append((((num % 1000) * 10 + num // 1000), s + 'L'))
        dslr.append((((num % 10) * 1000 + num // 10), s + 'R'))
        
        for i in range(4):
            if dslr[i][0] == b:
                print(dslr[i][1])
                break
            if memo[dslr[i][0]] == -1:
                memo[dslr[i][0]] = cnt
                dq.append(dslr[i])
        else:
            continue
        break