from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    n = 101
    memo = [[0 for _ in range(n)] for _ in range(n)]

    characterX <<= 1
    characterY <<= 1
    itemX <<= 1
    itemY <<= 1
    for x1, y1, x2, y2 in rectangle:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        x1 <<= 1
        x2 <<= 1
        y1 <<= 1
        y2 <<= 1

        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                memo[i][j] = 1

        for i in range(x1, x2 + 1):
            if not memo[i][y1]:
                memo[i][y1] = 2
            if not memo[i][y2]:
                memo[i][y2] = 2

        for j in range(y1, y2 + 1):
            if not memo[x1][j]:
                memo[x1][j] = 2
            if not memo[x2][j]:
                memo[x2][j] = 2

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[characterX][characterY] = True

    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    dq = deque([(characterX, characterY)])
    answer = 0

    while dq:
        answer += 1
        for _ in range(len(dq)):
            x, y = dq.popleft()

            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if a < 0 or a > n - 1:
                    continue
                if b < 0 or b > n - 1:
                    continue
                if memo[a][b] != 2:
                    continue

                if a == itemX and b == itemY:
                    return answer >> 1

                if visited[a][b]:
                    continue
                visited[a][b] = True

                dq.append((a, b))

    return -1
