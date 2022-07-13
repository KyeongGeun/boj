from collections import deque
import sys
input = sys.stdin.readline


class Marble:
    def __init__(self, rx, ry, bx, by, cnt):
        self.rx = rx
        self.ry = ry
        self.bx = bx
        self.by = by
        self.cnt = cnt


def move(m, d):
    nm = Marble(m.rx, m.ry, m.bx, m.by, m.cnt)

    cntr, cntb = 0, 0

    while board[nm.rx][nm.ry] != '#' and board[nm.rx][nm.ry] != 'O':
        nm.rx += dx[d]
        nm.ry += dy[d]
        cntr += 1
    if board[nm.rx][nm.ry] == '#':
        nm.rx -= dx[d]
        nm.ry -= dy[d]

    while board[nm.bx][nm.by] != '#' and board[nm.bx][nm.by] != 'O':
        nm.bx += dx[d]
        nm.by += dy[d]
        cntb += 1
    if board[nm.bx][nm.by] == '#':
        nm.bx -= dx[d]
        nm.by -= dy[d]

    if board[nm.rx][nm.ry] != 'O' and nm.rx == nm.bx and nm.ry == nm.by:
        if cntr < cntb:
            nm.bx -= dx[d]
            nm.by -= dy[d]
        else:
            nm.rx -= dx[d]
            nm.ry -= dy[d]

    nm.cnt += 1

    return nm


n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dq = deque()
dq.append(Marble(rx, ry, bx, by, 0))

visited = [[[[[False for _ in range(4)] for _ in range(
    m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

while dq:
    marble = dq.popleft()

    for i in range(4):
        nm = move(marble, i)

        if nm.cnt > 10:
            continue

        if visited[nm.rx][nm.ry][nm.bx][nm.by][i]:
            continue
        visited[nm.rx][nm.ry][nm.bx][nm.by][i] = True

        if board[nm.bx][nm.by] == 'O':
            continue

        if board[nm.rx][nm.ry] == 'O':
            print(nm.cnt)
            exit(0)

        dq.append(nm)

print(-1)
