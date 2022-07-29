from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sand = [list(input().rstrip()) for _ in range(n)]
sand = [[0 if sand[i][j] == '.' else int(
    sand[i][j]) for j in range(m)] for i in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

dq = deque()

for i in range(n):
    for j in range(m):
        if sand[i][j] == 0:
            dq.append((i, j))

ans = -1
while dq:
    ans += 1
    for _ in range(len(dq)):
        x, y = dq.popleft()

        for i in range(8):
            a = x + dx[i]
            b = y + dy[i]

            if a < 1 or a > n - 2:
                continue
            if b < 1 or b > m - 2:
                continue
            if sand[a][b] == 9 or sand[a][b] < 1:
                continue

            sand[a][b] -= 1
            if sand[a][b] == 0:
                dq.append((a, b))

print(ans)
