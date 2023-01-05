class Solution {
    fun findMinArrowShots(points: Array<IntArray>): Int {
        points.sortBy { it[0] }
        var l = points[0][0]
        var r = points[0][1]

        var ans = 1
        for (arr in points) {
            if (r < arr[0]) {
                ans++
                r = arr[1]
            } else {
                r = minOf(r, arr[1])
            }
        }

        return ans
    }
}
