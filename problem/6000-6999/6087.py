import heapq
import sys
input = sys.stdin.readline

w, h = map(int, input().split())

li = [list(input().rstrip()) for _ in range(h)]

hq = []

for i in range(h):
    for j in range(w):
        if li[i][j] == 'C':
            hq.append((0, i, j, -1))
            li[i][j] = '*'
            start = (i, j)
            break
    else:
        continue
    break

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[[False for _ in range(4)] for _ in range(w)] for _ in range(h)]
while hq:
    dis, x, y, dir = heapq.heappop(hq)

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if a < 0 or a > h - 1:
            continue
        if b < 0 or b > w - 1:
            continue
        if li[a][b] == '*':
            continue
        if visited[a][b][i]:
            continue
        visited[a][b][i] = True

        new_dis = dis
        if dir != i and dir != -1:
            new_dis += 1

        if li[a][b] == 'C':
            print(new_dis)
            exit(0)

        heapq.heappush(hq, (new_dis, a, b, i))
