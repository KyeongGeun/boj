class Solution {
    fun removeCoveredIntervals(intervals: Array<IntArray>): Int {
        intervals.sortWith(compareBy({ it[0] }, { -it[1] }))

        var right = intervals[0][1]
        var ans = 1
        for (interval in intervals) {
            if (right < interval[1]) {
                right = interval[1]
                ans++
            }
        }

        return ans
    }
}
