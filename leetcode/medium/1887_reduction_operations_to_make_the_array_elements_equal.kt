class Solution {
    fun reductionOperations(nums: IntArray): Int {
        val map = mutableMapOf<Int, Int>()
        for (num in nums) {
            map[num] = map.getOrDefault(num, 0) + 1
        }

        var ans = 0
        var cur = 0
        for (e in map.entries.sortedBy { -it.key }) {
            ans += cur
            cur += e.value
        }
        
        return ans
    }
}
