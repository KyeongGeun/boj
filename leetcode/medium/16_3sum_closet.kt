import kotlin.math.abs

class Solution {
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        nums.sort()
        var minv = Integer.MAX_VALUE
        var ans = 0
        
        for (i in 0 until nums.size - 2) {
            var l = i + 1
            var r = nums.size - 1
            
            while (l < r) {
                val cur = nums[i] + nums[l] + nums[r]
                val d = abs(target - cur)
                
                if (minv > d) {
                    minv = d
                    ans = cur
                }
                if (target > cur) l++
                else if (target < cur) r--
                else return target
            }
        }

        return ans
    }
}
