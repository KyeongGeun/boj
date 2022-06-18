import heapq
import sys
input = sys.stdin.readline


def dijk(i, j):
    hq = [(0, i, j)]

    while hq:
        cur_dis, x, y = heapq.heappop(hq)

        if cur_dis > dis[x][y]:
            continue

        for i in range(4):
            a, b = x + dx[i], y + dy[i]

            if a < 0 or a >= n:
                continue
            if b < 0 or b >= m:
                continue

            if li[a][b] == '1':
                new_dis = cur_dis + 1
            else:
                new_dis = cur_dis

            if dis[a][b] > new_dis:
                dis[a][b] = new_dis

                if a == n - 1 and b == m - 1:
                    return new_dis

                heapq.heappush(hq, (new_dis, a, b))

    return dis[n - 1][m - 1]


m, n = map(int, input().split())
li = [input().rstrip() for _ in range(n)]
dis = [[float('inf') for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dis[0][0] = 0
print(dijk(0, 0))
