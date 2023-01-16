class Solution {
    fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        val left = mutableListOf<IntArray>()
        val right = mutableListOf<IntArray>()
        for (interval in intervals)
            if (interval[1] < newInterval[0]) left.add(interval)
        for (interval in intervals.reversed())
            if (interval[0] > newInterval[1]) right.add(interval)

        val ans = mutableListOf<IntArray>()
        ans.addAll(left)
        
        var l = newInterval[0]
        var r = newInterval[1]
        if (intervals.size > left.size)
            l = minOf(l, intervals[left.size][0])
        if (intervals.size > right.size)
            r = maxOf(r, intervals[intervals.size - right.size - 1][1])
        ans.add(intArrayOf(l, r))
        
        ans.addAll(right.reversed())

        return ans.toTypedArray()
    }
}
