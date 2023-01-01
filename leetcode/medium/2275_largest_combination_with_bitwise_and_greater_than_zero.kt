class Solution {
    fun largestCombination(candidates: IntArray): Int {
        var ans = 1
        for (i in 0..25) {
            var cur = 0
            for (num in candidates)
                if (num and (1 shl i) != 0)
                    cur++
            ans = maxOf(ans, cur)
        }

        return ans
    }
}
