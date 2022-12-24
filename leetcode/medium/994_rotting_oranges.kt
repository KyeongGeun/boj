class Solution {
    fun orangesRotting(grid: Array<IntArray>): Int {
        val dq = ArrayDeque<Pair<Int, Int>>()

        for (i in grid.indices) {
            for (j in grid[i].indices) {
                if (grid[i][j] == 2) dq.add(i to j)
            }
        }

        val dx = arrayOf(1, -1, 0, 0)
        val dy = arrayOf(0, 0, 1, -1)

        var ans = 0
        while (!dq.isEmpty()) {
            for (a in 1..dq.size) {
                val (x, y) = dq.removeFirst()

                for (i in dx.indices) {
                    val nx = x + dx[i]
                    val ny = y + dy[i]

                    if (nx < 0 || nx > grid.size - 1) continue
                    if (ny < 0 || ny > grid[0].size - 1) continue
                    if (grid[nx][ny] != 1) continue
                    grid[nx][ny] = 2
                    dq.add(nx to ny)
                }
            }
            if (!dq.isEmpty()) ans += 1
        }

        for (i in grid.indices) {
            for (j in grid[i].indices) {
                if (grid[i][j] == 1) return -1
            }
        }

        return ans
    }
}
