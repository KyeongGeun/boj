from collections import deque
from copy import deepcopy
import sys

import sys
input = sys.stdin.readline

def bfs():

    dq = deque([(0, 0, 0)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]


    while dq:
        x, y, z = dq.popleft()
        
        if x == n - 1 and y == m - 1:
            print(li[z][x][y])
            break

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m:
                if li[z][a][b] == '1':
                    if z == 0:
                        li[1][a][b] = li[z][x][y] + 1
                        dq.append((a, b, 1))
                elif li[z][a][b] == '0':
                    li[z][a][b] = li[z][x][y] + 1
                    dq.append((a, b, z))
    else:
        print(-1)

n, m = map(int, input().split())

li = [list(input().rstrip()) for _ in range(n)]
li = [li] + [deepcopy(li)]

li[0][0][0] = 1
bfs()