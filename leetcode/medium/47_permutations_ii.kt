class Solution {

    val set = mutableSetOf<List<Int>>()

    private fun recur(cur: MutableList<Int>, nums: IntArray, bit: Int) {
        if (cur.size >= nums.size) {
            set.add(cur.toList())
            return
        }

        for (i in nums.indices) {
            if ((1 shl i) and bit != 0) continue

            cur.add(nums[i])
            recur(cur, nums, bit or (1 shl i))
            cur.removeAt(cur.lastIndex)
        }
    }

    fun permuteUnique(nums: IntArray): List<List<Int>> {
        recur(mutableListOf(), nums, 0)
        return set.toList()
    }

}