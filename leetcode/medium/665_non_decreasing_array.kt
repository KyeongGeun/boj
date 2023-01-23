class Solution {
    fun checkPossibility(nums: IntArray): Boolean {
        var flag = false
        for (i in 1 until nums.size) {
            if (nums[i - 1] > nums[i]) {
                if (flag) return false
                if (i != 1 && nums[i - 2] > nums[i]) 
                    nums[i] = nums[i - 1]
                flag = true
            }
        }

        return true
    }
}
