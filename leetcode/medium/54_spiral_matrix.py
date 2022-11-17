from collections import deque


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)

        ans = []
        x, y, d = 0, 0, 0
        while True:
            ans.append(matrix[x][y])
            visited[x][y] = True
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1 or visited[nx][ny]:
                d = (d + 1) % 4
                nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1 or visited[nx][ny]:
                break

            x, y = nx, ny

        return ans
