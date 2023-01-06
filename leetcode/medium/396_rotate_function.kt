class Solution {
    fun maxRotateFunction(nums: IntArray): Int {
        val sum = nums.sum()
        var cur = 0
        for (i in 1 until nums.size) {
            cur += i * nums[i]
        }

        var ans = cur
        for (i in nums.size - 1 downTo 1) {
            cur += sum - nums[i] * nums.size
            ans = maxOf(ans, cur)
        }

        return ans
    }
}
