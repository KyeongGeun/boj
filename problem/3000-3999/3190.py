from collections import deque
import sys
input = sys.stdin.readline


def move():
    x, y = dq[-1]
    x += dx[dir]
    y += dy[dir]

    if x < 0 or x > n - 1 or y < 0 or y > n - 1 or board[x][y] == 1:
        print(sec)
        exit(0)

    if board[x][y] != 2:
        i, j = dq.popleft()
        board[i][j] = 0

    dq.append((x, y))
    board[x][y] = 1


n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
sec = 0
dir = 0
dq = deque()
dq.append((0, 0))
for _ in range(int(input())):
    a, b = input().split()
    a = int(a)

    while sec < a:
        sec += 1
        move()

    if b == 'L':
        dir = (dir - 1) % 4
    else:
        dir = (dir + 1) % 4

while True:
    sec += 1
    move()
