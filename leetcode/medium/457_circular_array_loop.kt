class Solution {
    fun circularArrayLoop(nums: IntArray): Boolean {
        val visited = Array(nums.size) { false }
        for (i in nums.indices) {
            if (visited[i]) continue
            visited[i] = true

            val set = mutableSetOf<Int>()
            var cur = i
            if (nums[i] > 0) {
                while (nums[cur] > 0) {
                    if (nums[cur] % nums.size == 0) break
                    set.add(cur)
                    cur = (cur + nums[cur]) % nums.size
                    visited[cur] = true
                    if (cur in set) return true
                }
            } else {
                while (nums[cur] < 0) {
                    if (nums[cur] % nums.size == 0) break
                    set.add(cur)
                    cur = (cur + nums[cur]) % nums.size
                    if (cur < 0) cur += nums.size
                    visited[cur] = true
                    if (cur in set) return true
                }
            }
        }

        return false
    }
}
