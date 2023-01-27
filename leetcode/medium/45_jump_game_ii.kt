class Solution {
    fun jump(nums: IntArray): Int {
        var ans = 0
        var cur = nums[0]
        var end = 0
        for (i in 0..nums.size - 2) {
            cur = maxOf(cur, i + nums[i])

            if (i == end) {
                end = cur
                ans++
            }
        }

        return ans
    }
}
