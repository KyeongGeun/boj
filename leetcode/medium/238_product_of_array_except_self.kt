class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        var product = 1
        var zero = 0
        for (num in nums) {
            if (num == 0) zero += 1
            else product *= num
        }

        return if (zero > 1) IntArray(nums.size) { 0 }
        else if (zero == 1) IntArray(nums.size) { i -> if (nums[i] == 0) product else 0 }
        else IntArray(nums.size) { i -> if (nums[i] == 0) product else product / nums[i] }
    }
}
