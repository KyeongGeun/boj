from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())

li = [list(input().rstrip()) for _ in range(h)]

dq = deque()
for i in range(h):
    for j in range(w):
        if li[i][j] == 'D':
            dq.append((i, j, ''))
            break

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dir = {'W': 0, 'A': 1, 'S': 2, 'D': 3}

for _ in range(int(input())):
    inp = input().split()
    for _ in range(len(dq)):
        x, y, c = dq.popleft()
        for s in inp:
            a = x + dx[dir[s]]
            b = y + dy[dir[s]]

            if a < 0 or a > h - 1:
                continue
            if b < 0 or b > w - 1:
                continue
            if li[a][b] == '@':
                continue
            if li[a][b] == 'Z':
                print('YES')
                print(c + s)
                exit(0)

            dq.append((a, b, c + s))

print('NO')
