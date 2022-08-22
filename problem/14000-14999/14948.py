import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

if n == 1 and m == 1:
    print(li[0][0])
    exit(0)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dx2 = [2, 0, -2, 0]
dy2 = [0, 2, 0, -2]

hq = [(li[0][0], -1, 0, 0)]
memo = [[[float('inf') for _ in range(2)] for _ in range(m)] for _ in range(n)]
memo[0][0][0] = 0
memo[0][0][1] = 0

while hq:
    v, f, x, y = heapq.heappop(hq)
    f = -f

    if f:
        for i in range(4):
            a = x + dx2[i]
            b = y + dy2[i]

            if a < 0 or a > n - 1:
                continue
            if b < 0 or b > m - 1:
                continue

            s = max(v, li[a][b])

            if a == n - 1 and b == m - 1:
                print(s)
                exit(0)

            if memo[a][b][0] <= s:
                continue
            memo[a][b][0] = s

            heapq.heappush(hq, (s, 0, a, b))

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if a < 0 or a > n - 1:
            continue
        if b < 0 or b > m - 1:
            continue

        s = max(v, li[a][b])

        if a == n - 1 and b == m - 1:
            print(s)
            exit(0)

        if memo[a][b][f] <= s:
            continue
        memo[a][b][f] = s

        heapq.heappush(hq, (s, -f, a, b))
