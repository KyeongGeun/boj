class Solution {
    fun sumOfBeauties(nums: IntArray): Int {
        var ans = 0
        for (i in 1..nums.size - 2)
            if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1])
                ans++

        val set = mutableSetOf<Int>()
        var max = nums[0]
        for (i in 1..nums.size - 2)
            if (max < nums[i]) {
                set.add(i)
                max = nums[i]
            }
            
        var min = nums[nums.size - 1]
        for (i in nums.size - 2 downTo 1) {
            if (nums[i] < min && i in set) ans++
            min = minOf(min, nums[i])
        }

        return ans
    }
}
