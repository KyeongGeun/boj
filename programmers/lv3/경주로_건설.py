from collections import deque


def solution(board):
    n = len(board)

    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    memo = [[[float('inf') for _ in range(4)] for _ in range(n)]
            for _ in range(n)]
    dq = deque([(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3)])
    memo[0][0] = [0, 0, 0, 0]

    while dq:
        x, y, d = dq.popleft()
        p = memo[x][y][d]

        for i in range(4):
            a, b = x + dx[i], y + dy[i]

            if a < 0 or a > n - 1:
                continue
            if b < 0 or b > n - 1:
                continue
            if board[a][b] == 1:
                continue
            if memo[a][b][i] <= p + 100:
                continue

            if d == i:
                memo[a][b][i] = p + 100
                dq.appendleft((a, b, i))
            else:
                if memo[a][b][i] <= p + 600:
                    continue
                memo[a][b][i] = p + 600
                dq.append((a, b, i))

    return min(memo[n - 1][n - 1])
