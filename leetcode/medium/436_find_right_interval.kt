class Solution {
    fun findRightInterval(intervals: Array<IntArray>): IntArray {
        val map = intervals.mapIndexed { idx, arr -> arr[0] to idx }.groupBy ({ it.first }, { it.second })
        val starts = intervals.map { it[0] }.sorted()
        val ans = IntArray(intervals.size)

        for (i in intervals.indices) {
            val idx = starts.binarySearch(intervals[i][1])
            if (idx < 0) {
                if (-idx > starts.size) ans[i] = -1
                else ans[i] = map[starts[-idx - 1]]!![0]
            } else {
                ans[i] = map[starts[idx]]!![0]
            }
        }

        return ans
    }
}
