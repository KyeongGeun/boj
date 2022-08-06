from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    dq = deque()
    dq.append((0, 0))

    while dq:
        x, y = dq.popleft()
        for i in range(2):
            a = x + dx[i]
            b = y + dy[i]

            if a > n - 1 or b > n - 1:
                continue

            if (a + b) % 2 == 1:
                maxDp[a][b] = max(maxDp[a][b], maxDp[x][y])
                minDp[a][b] = min(minDp[a][b], minDp[x][y])

            else:
                oper = board[x][y]
                num = int(board[a][b])
                if oper == '+':
                    maxDp[a][b] = max(maxDp[a][b], maxDp[x][y] + num)
                    minDp[a][b] = min(minDp[a][b], minDp[x][y] + num)
                elif oper == '-':
                    maxDp[a][b] = max(maxDp[a][b], maxDp[x][y] - num)
                    minDp[a][b] = min(minDp[a][b], minDp[x][y] - num)
                elif oper == '*':
                    maxDp[a][b] = max(maxDp[a][b], maxDp[x][y] * num)
                    minDp[a][b] = min(minDp[a][b], minDp[x][y] * num)

            dq.append((a, b))


n = int(input())

board = [input().split() for _ in range(n)]
maxDp = [[-float('inf') for _ in range(n)] for _ in range(n)]
maxDp[0][0] = int(board[0][0])
minDp = [[float('inf') for _ in range(n)] for _ in range(n)]
minDp[0][0] = int(board[0][0])

dx = [1, 0]
dy = [0, 1]

bfs()

print(maxDp[n - 1][n - 1], minDp[n - 1][n - 1])
