from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        dx = (1, 0, -1, 0)
        dy = (0, 1, 0, -1)

        def dfs(i, j, grid):
            grid[i][j] = '0'
            dq = deque([(i, j)])

            while dq:
                x, y = dq.popleft()

                for d in range(4):
                    a = x + dx[d]
                    b = y + dy[d]

                    if a < 0 or a > m - 1:
                        continue
                    if b < 0 or b > n - 1:
                        continue

                    if grid[a][b] == '0':
                        continue

                    grid[a][b] = '0'
                    dq.append((a, b))

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j, grid)
                    ans += 1

        return ans
