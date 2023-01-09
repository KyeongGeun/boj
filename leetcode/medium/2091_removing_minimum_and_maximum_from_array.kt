class Solution {
    fun minimumDeletions(nums: IntArray): Int {
        var min = 100000
        var minIdx = 0
        var max = -100000
        var maxIdx = 0
        for (i in nums.indices) {
            if (min > nums[i]) {
                min = nums[i]
                minIdx = i
            }
            if (max < nums[i]) {
                max = nums[i]
                maxIdx = i
            }
        }

        if (minIdx == maxIdx)
            return minOf(minIdx + 1, nums.size - minIdx)
        if (minIdx + 1 <= minOf(maxIdx + 1, nums.size - maxIdx))
            return minIdx + 1 + minOf(maxIdx - minIdx, nums.size - maxIdx)
        if (nums.size - minIdx <= minOf(maxIdx + 1, nums.size - maxIdx))
            return nums.size - minIdx + minOf(maxIdx + 1, minIdx - maxIdx)
        if (maxIdx + 1 <= minOf(minIdx + 1, nums.size - minIdx))
            return maxIdx + 1 + minOf(minIdx - maxIdx, nums.size - minIdx)
        return nums.size - maxIdx + minOf(minIdx + 1, maxIdx - minIdx)
    }
}
