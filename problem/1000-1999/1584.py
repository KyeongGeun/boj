from collections import deque
import sys
input = sys.stdin.readline

li = [[0 for _ in range(501)] for _ in range(501)]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            li[i][j] = 1

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            li[i][j] = 2

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
inf = float('inf')
visited = [[inf for _ in range(501)] for _ in range(501)]
visited[0][0] = 0

dq = deque([(0, 0, 0)])
while dq:
    h, x, y = dq.popleft()

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if a < 0 or a > 500:
            continue
        if b < 0 or b > 500:
            continue
        if li[a][b] == 2:
            continue

        if visited[a][b] > h + li[a][b]:
            visited[a][b] = h + li[a][b]

            if a == 500 and b == 500:
                continue
            if li[a][b] == 1:
                dq.append((h + 1, a, b))
            else:
                dq.appendleft((h, a, b))


ans = visited[500][500]
print(-1 if ans == inf else ans)
