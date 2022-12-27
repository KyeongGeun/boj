class Solution {
    fun maximumBags(capacity: IntArray, rocks: IntArray, additionalRocks: Int): Int {
        val pairs = capacity.mapIndexed { i, c -> rocks[i] to c }
            .sortedBy { it.second - it.first }

        var ans = 0
        var remain = additionalRocks
        for ((r, c) in pairs) {
            val cur = c - r
            if (cur <= remain) {
                remain -= cur
                ans++
            } else break
        }

        return ans
    }
}
